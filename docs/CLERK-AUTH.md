
# Clerk Authentication

The frontend uses Clerk JS for sign-in/sign-up. The backend validates Clerk JWTs for protected endpoints.

## Environment

All secrets and environment variables are managed in `env` and `env.production` files.

## Auth Enforcement

Backend implementation: `backend/src/infrastructure/clerk_auth.py`

- `verify_clerk_token`: Validates Bearer token format and verifies JWT signature using Clerk JWKS.
- `get_optional_user`: Returns authenticated user payload if token is valid, or `None` if not.

## Local Development

To bypass auth locally, set `SKIP_AUTH=true` in your environment file. This skips JWT validation and returns a mock local payload.

## Protected API Routes

Routes in `backend/src/adapters/api/metrics.py` are protected with `Depends(verify_clerk_token)`.
