"""
Clerk JWT validation middleware for FastAPI

Validates JWT tokens issued by Clerk
"""

import os
from typing import Optional
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from jose import jwt, JWTError
import requests

security = HTTPBearer()

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


async def verify_clerk_token(credentials: HTTPAuthCredentials = Depends(security)) -> dict:
    """
    Verify Clerk JWT token and return decoded token payload
    
    Usage:
        @app.get("/protected")
        async def protected_route(token: dict = Depends(verify_clerk_token)):
            user_id = token.get("sub")
            ...
    """
    token = credentials.credentials
    clerk_domain = os.getenv("CLERK_DOMAIN", "")
    
    if not clerk_domain:
        raise HTTPException(status_code=500, detail="CLERK_DOMAIN not configured")
    
    try:
        jwks = await get_clerk_jwks()
        
        # Get the key ID from token header
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        
        if not kid:
            raise JWTError("Token missing 'kid' header")
        
        # Find the matching public key
        key = None
        for jwk in jwks.get("keys", []):
            if jwk["kid"] == kid:
                key = jwt.algorithms.RSAAlgorithm.from_jwk(jwk)
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
        
        return payload
        
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")


async def get_optional_user(
    credentials: Optional[HTTPAuthCredentials] = Depends(security)
) -> Optional[dict]:
    """
    Optional authentication - returns user if token provided, None otherwise
    
    Usage:
        @app.get("/public")
        async def public_route(user: Optional[dict] = Depends(get_optional_user)):
            if user:
                user_id = user.get("sub")
            ...
    """
    if not credentials:
        return None
    
    try:
        return await verify_clerk_token(credentials)
    except HTTPException:
        return None
