"""
Clerk JWT validation middleware for FastAPI

Validates JWT tokens issued by Clerk
"""

import os
import logging
import time
from typing import Optional
from fastapi import HTTPException, Depends, Request
from jose import jwt, JWTError, jwk
import requests

# Cache for Clerk's public key (valid for 24 hours)
_clerk_jwks_cache = None
_clerk_jwks_cache_time = None
_auth_failures_by_ip: dict[str, list[float]] = {}
logger = logging.getLogger(__name__)


def _get_allowed_domains() -> list[str]:
    """Read and normalize the allowed email domains from environment."""
    allowed_domains = os.getenv("ALLOWED_EMAIL_DOMAIN", "students.iaac.net")
    return [domain.strip().lower() for domain in allowed_domains.split(",") if domain.strip()]


def _get_auth_rate_limit_window_seconds() -> int:
    value = os.getenv("AUTH_FAILURE_WINDOW_SECONDS", "300")
    try:
        return max(1, int(value))
    except ValueError:
        return 300


def _get_auth_rate_limit_max_attempts() -> int:
    value = os.getenv("AUTH_FAILURE_MAX_ATTEMPTS", "20")
    try:
        return max(1, int(value))
    except ValueError:
        return 20


def _get_client_ip(request: Request) -> str:
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        first_ip = forwarded_for.split(",", 1)[0].strip()
        if first_ip:
            return first_ip

    if request.client and request.client.host:
        return request.client.host

    return "unknown"


def _prune_old_failures(ip_address: str, now: float, window_seconds: int) -> None:
    failures = _auth_failures_by_ip.get(ip_address, [])
    cutoff = now - window_seconds
    active = [timestamp for timestamp in failures if timestamp >= cutoff]
    if active:
        _auth_failures_by_ip[ip_address] = active
    elif ip_address in _auth_failures_by_ip:
        del _auth_failures_by_ip[ip_address]


def _record_auth_failure(ip_address: str, now: Optional[float] = None) -> None:
    current_time = time.time() if now is None else now
    window_seconds = _get_auth_rate_limit_window_seconds()
    _prune_old_failures(ip_address, current_time, window_seconds)
    _auth_failures_by_ip.setdefault(ip_address, []).append(current_time)


def _is_auth_rate_limited(ip_address: str, now: Optional[float] = None) -> bool:
    current_time = time.time() if now is None else now
    window_seconds = _get_auth_rate_limit_window_seconds()
    max_attempts = _get_auth_rate_limit_max_attempts()
    _prune_old_failures(ip_address, current_time, window_seconds)
    return len(_auth_failures_by_ip.get(ip_address, [])) >= max_attempts


def _clear_auth_failures(ip_address: str) -> None:
    _auth_failures_by_ip.pop(ip_address, None)


def _extract_email_from_payload(payload: dict) -> Optional[str]:
    """Extract email from Clerk token payload across common claim shapes."""
    direct_email = payload.get("email") or payload.get("email_address")
    if isinstance(direct_email, str) and direct_email.strip():
        return direct_email.strip().lower()

    email_addresses = payload.get("email_addresses")
    primary_email_id = payload.get("primary_email_address_id")
    if primary_email_id and isinstance(email_addresses, list):
        for item in email_addresses:
            if not isinstance(item, dict):
                continue
            if item.get("id") == primary_email_id:
                email = item.get("email_address") or item.get("email")
                if isinstance(email, str) and email.strip():
                    return email.strip().lower()

    if isinstance(email_addresses, list):
        for item in email_addresses:
            if not isinstance(item, dict):
                continue
            email = item.get("email_address") or item.get("email")
            if isinstance(email, str) and email.strip():
                return email.strip().lower()

    return None


def _log_auth_failure(reason: str, payload: Optional[dict] = None) -> None:
    """Log auth failures without exposing secrets."""
    if isinstance(payload, dict):
        user_id = payload.get("sub", "unknown")
        email = _extract_email_from_payload(payload) or "unknown"
    else:
        user_id = "unknown"
        email = "unknown"

    logger.warning("Authentication failed: %s | user_id=%s | email=%s", reason, user_id, email)


def _enforce_domain_authorization(payload: dict) -> dict:
    """Enforce allowed email-domain policy on a decoded token payload."""
    allowed_domains = _get_allowed_domains()
    if not allowed_domains:
        return payload

    email = _extract_email_from_payload(payload)
    if not email:
        _log_auth_failure("Email claim missing", payload)
        raise HTTPException(status_code=403, detail="Email claim missing")

    if not any(email.endswith(f"@{domain}") for domain in allowed_domains):
        _log_auth_failure(f"Email domain not allowed (allowed={allowed_domains})", payload)
        raise HTTPException(status_code=403, detail="IAAC email required")

    return payload

async def get_clerk_jwks():
    """Fetch Clerk's JWKS (public keys) for JWT verification"""
    import time
    global _clerk_jwks_cache, _clerk_jwks_cache_time
    
    # Return cached JWKS if still valid (cache for 1 hour)
    if _clerk_jwks_cache and _clerk_jwks_cache_time:
        if time.time() - _clerk_jwks_cache_time < 3600:
            return _clerk_jwks_cache
    
    clerk_domain = os.getenv("CLERK_DOMAIN", "")
    if not clerk_domain:
        raise HTTPException(status_code=500, detail="CLERK_DOMAIN environment variable not set")
    
    try:
        response = requests.get(f"https://{clerk_domain}/.well-known/jwks.json")
        response.raise_for_status()
        _clerk_jwks_cache = response.json()
        _clerk_jwks_cache_time = time.time()
        return _clerk_jwks_cache
    except Exception as e:
        logger.exception("Failed to fetch Clerk JWKS")
        raise HTTPException(status_code=500, detail="Failed to fetch Clerk JWKS")


async def verify_clerk_token(request: Request) -> dict:
    """
    Verify Clerk JWT token and return decoded token payload
    
    For local development: authentication is optional. If no Authorization header
    is provided, a mock token is returned. Use SKIP_AUTH=true to disable all checks.
    
    Usage:
        @app.get("/protected")
        async def protected_route(token: dict = Depends(verify_clerk_token)):
            user_id = token.get("sub")
            ...
    """
    # Skip all authentication if SKIP_AUTH is set (local development only)
    if os.getenv("SKIP_AUTH", "").lower() == "true":
        return {"sub": "local-dev", "email": "dev@iaac.net"}

    client_ip = _get_client_ip(request)
    if _is_auth_rate_limited(client_ip):
        logger.warning("Authentication blocked by rate limit | ip=%s", client_ip)
        raise HTTPException(status_code=429, detail="Too many authentication failures. Try again later.")
    
    # Check for Authorization header
    auth_header = request.headers.get("authorization")

    if not auth_header:
        logger.warning("Authentication failed: Missing authorization header")
        _record_auth_failure(client_ip)
        raise HTTPException(status_code=401, detail="Missing authorization header")
    
    # If Authorization header IS provided, validate it
    clerk_domain = os.getenv("CLERK_DOMAIN", "").strip()
    if not clerk_domain:
        logger.error("Authentication failed: CLERK_DOMAIN environment variable not set")
        raise HTTPException(status_code=500, detail="CLERK_DOMAIN environment variable not set")
    
    try:
        scheme, token = auth_header.split(" ", 1)
        if scheme.lower() != "bearer":
            logger.warning("Authentication failed: Invalid authentication scheme")
            _record_auth_failure(client_ip)
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    except ValueError:
        logger.warning("Authentication failed: Invalid authorization header format")
        _record_auth_failure(client_ip)
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    try:
        jwks = await get_clerk_jwks()
        
        # Get the key ID from token header
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        
        if not kid:
            raise JWTError("Token missing 'kid' header")
        
        # Find the matching public key
        key = None
        for jwk_data in jwks.get("keys", []):
            if jwk_data["kid"] == kid:
                key = jwk.construct(jwk_data)
                break
        
        if not key:
            raise JWTError(f"Unable to find matching key for kid: {kid}")
        
        # Verify and decode token
        audience = os.getenv("CLERK_FRONTEND_API_URL", "")
        issuer = os.getenv("CLERK_ISSUER", f"https://{clerk_domain}")

        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=audience or None,
            issuer=issuer
        )

        authorized_payload = _enforce_domain_authorization(payload)
        _clear_auth_failures(client_ip)
        return authorized_payload

    except HTTPException:
        _record_auth_failure(client_ip)
        raise
        
    except JWTError as e:
        logger.warning("Authentication failed: Invalid token (%s)", str(e))
        _record_auth_failure(client_ip)
        raise HTTPException(status_code=401, detail="Invalid token")


async def get_optional_user(request: Request) -> Optional[dict]:
    """
    Optional authentication - returns user if token provided, None otherwise
    
    Usage:
        @app.get("/public")
        async def public_route(user: Optional[dict] = Depends(get_optional_user)):
            if user:
                user_id = user.get("sub")
            ...
    """
    auth_header = request.headers.get("authorization")
    if not auth_header:
        return None
    
    try:
        scheme, token = auth_header.split(" ", 1)
        if scheme.lower() != "bearer":
            logger.warning("Optional auth failed: Invalid authentication scheme")
            return None
    except ValueError:
        logger.warning("Optional auth failed: Invalid authorization header format")
        return None
    
    # Create a minimal request-like object for verify_clerk_token
    try:
        # Temporarily modify request headers for verification
        clerk_domain = os.getenv("CLERK_DOMAIN", "")
        if not clerk_domain:
            logger.warning("Optional auth failed: CLERK_DOMAIN environment variable not set")
            return None
        
        jwks = await get_clerk_jwks()
        
        # Get the key ID from token header
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        
        if not kid:
            logger.warning("Optional auth failed: Token missing 'kid' header")
            return None
        
        # Find the matching public key
        key = None
        for jwk_data in jwks.get("keys", []):
            if jwk_data["kid"] == kid:
                key = jwk.construct(jwk_data)
                break
        
        if not key:
            logger.warning("Optional auth failed: No matching key for token kid")
            return None
        
        # Verify and decode token
        audience = os.getenv("CLERK_FRONTEND_API_URL", "")
        issuer = os.getenv("CLERK_ISSUER", f"https://{clerk_domain}")

        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=audience or None,
            issuer=issuer
        )

        return _enforce_domain_authorization(payload)
    except Exception:
        logger.warning("Optional auth failed: Token verification error")
        return None
