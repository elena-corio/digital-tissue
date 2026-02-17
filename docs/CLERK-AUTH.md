# Clerk Authentication

## Overview

The frontend uses Clerk JS for sign-in/sign-up.
The backend validates Clerk JWTs and enforces email-domain authorization on protected endpoints.

## Backend Environment

Set these in `backend/.env`:

```env
CLERK_DOMAIN=your-app.clerk.accounts.dev
CLERK_ISSUER=https://your-app.clerk.accounts.dev
CLERK_FRONTEND_API_URL=http://localhost:5174
ALLOWED_EMAIL_DOMAIN=students.iaac.net
```

Notes:
- `ALLOWED_EMAIL_DOMAIN` supports multiple values separated by commas.
- Example: `ALLOWED_EMAIL_DOMAIN=students.iaac.net,iaac.net`

## Auth Enforcement

Implementation: `backend/src/infrastructure/clerk_auth.py`

### Required auth

`verify_clerk_token`:
- validates Bearer token format
- verifies JWT signature using Clerk JWKS
- validates issuer and audience
- enforces allowed email domains

### Optional auth

`get_optional_user`:
- returns authenticated user payload only if token is valid and domain is allowed
- returns `None` for invalid/missing tokens or unauthorized domains

## Domain Authorization

Authorization uses claims from Clerk payload and resolves email in this order:
1. `email` or `email_address`
2. `primary_email_address_id` lookup inside `email_addresses`
3. first valid entry in `email_addresses`

If no allowed domain matches, backend returns `403`.

## Local Development

To bypass auth locally, set:

```env
SKIP_AUTH=true
```

When enabled:
- JWT validation is skipped
- domain authorization is skipped
- a mock local payload is returned

## Auth Failure Logging

The backend logs auth failures without logging tokens.

Logged cases include:
- missing authorization header
- invalid auth scheme/header format
- JWT validation failures
- missing email claim
- disallowed email domain

## Protected API Routes

Routes in `backend/src/adapters/api/metrics.py` are protected with `Depends(verify_clerk_token)`:
- `GET /api/metrics`
- `GET /api/metrics/history`
- `GET /api/metrics/{version_id}`
- `POST /api/metrics/calculate`
