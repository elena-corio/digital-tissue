"""
Clerk JWT validation middleware for FastAPI

Validates JWT tokens issued by Clerk
"""

import os
from typing import Optional
from fastapi import HTTPException, Depends, Request
from jose import jwt, JWTError, jwk
import requests

# Cache for Clerk's public key (valid for 24 hours)
_clerk_jwks_cache = None
_clerk_jwks_cache_time = None

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
        raise HTTPException(status_code=500, detail=f"Failed to fetch Clerk JWKS: {str(e)}")


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
    # Skip all authentication if SKIP_AUTH is set
    if os.getenv("SKIP_AUTH", "").lower() == "true":
        return {"sub": "local-dev", "email": "dev@iaac.net"}
    
    # Check for Authorization header
    auth_header = request.headers.get("authorization")
    
    # If no auth header provided, allow local development by returning mock token
    if not auth_header:
        # Return a minimal mock token for local development (no auth required)
        return {"sub": "local-dev", "email": "dev@students.iaac.net"}
    
    # If Authorization header IS provided, validate it
    clerk_domain = os.getenv("CLERK_DOMAIN", "").strip()
    if not clerk_domain:
        # If Clerk not configured but header provided, still allow it
        return {"sub": "header-provided", "email": "user@students.iaac.net"}
    
    try:
        scheme, token = auth_header.split(" ", 1)
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    except ValueError:
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

        allowed_domains = os.getenv("ALLOWED_EMAIL_DOMAIN", "students.iaac.net")
        allowed_list = [d.strip().lower() for d in allowed_domains.split(",") if d.strip()]
        if allowed_list:
            email = payload.get("email") or payload.get("email_address")
            if not email:
                raise HTTPException(status_code=403, detail="Email claim missing")
            email = email.lower()
            if not any(email.endswith(f"@{domain}") for domain in allowed_list):
                raise HTTPException(status_code=403, detail="IAAC email required")
        
        return payload
        
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")


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
            return None
    except ValueError:
        return None
    
    # Create a minimal request-like object for verify_clerk_token
    try:
        # Temporarily modify request headers for verification
        clerk_domain = os.getenv("CLERK_DOMAIN", "")
        if not clerk_domain:
            return None
        
        jwks = await get_clerk_jwks()
        
        # Get the key ID from token header
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        
        if not kid:
            return None
        
        # Find the matching public key
        key = None
        for jwk_data in jwks.get("keys", []):
            if jwk_data["kid"] == kid:
                key = jwk.construct(jwk_data)
                break
        
        if not key:
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
        
        return payload
    except Exception:
        return None
