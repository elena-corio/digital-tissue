# Clerk Authentication (JS Integration)

## Overview

This project uses Clerk for authentication. The frontend loads Clerk JS directly and mounts the Sign In and Sign Up widgets. The backend validates Clerk JWTs for protected endpoints.

## Frontend Setup

### Environment

`frontend/.env`
```env
VITE_SPECKLE_SERVER=https://app.speckle.systems
VITE_API_URL=http://localhost:8000
VITE_CLERK_PUBLISHABLE_KEY=pk_test_YOUR_KEY_HERE
```

`frontend/.env.production`
```env
VITE_API_URL=https://digital-tissue.onrender.com
VITE_CLERK_PUBLISHABLE_KEY=
```

### Key Files

- `src/config/clerk.js` - publishable key
- `src/composables/useClerk.js` - Clerk JS initialization + helpers
- `src/views/SignIn.vue` - mounts Clerk Sign In widget
- `src/views/SignUp.vue` - mounts Clerk Sign Up widget
- `src/router/index.js` - protects `/workspace`
- `src/services/metricsApi.js` - sends Bearer token

### How the UI Works

The Sign In/Up views call `clerk.mountSignIn()` and `clerk.mountSignUp()` after Clerk is loaded.

### Getting a Session Token

```javascript
import { useClerk } from '@/composables/useClerk.js'

const { getSessionToken } = useClerk()
const token = await getSessionToken()
```

### Sending Auth Header

```javascript
const headers = {
    Authorization: `Bearer ${token}`
}
```

## Backend Setup

### Environment

`backend/.env`
```env
CLERK_DOMAIN=your-app.clerk.accounts.dev
CLERK_ISSUER=https://your-app.clerk.accounts.dev
CLERK_FRONTEND_API_URL=http://localhost:5173
ALLOWED_EMAIL_DOMAIN=students.iaac.net
```

### JWT Verification

Backend uses `backend/src/infrastructure/clerk_auth.py` to verify JWTs.
All `/api/metrics` endpoints are protected via dependencies in `backend/src/adapters/api/metrics.py`.

### Domain Restriction (Free)

If `ALLOWED_EMAIL_DOMAIN` is set, non-matching emails get `403`.

## Troubleshooting

- Publishable key must start with `pk_test_` or `pk_live_`
- If sign-in widget is blank, verify `VITE_CLERK_PUBLISHABLE_KEY`
- Ensure backend env vars are set before running FastAPI
    - sub: user ID
    - email: user email
    - name: user name
    - and other Clerk claims
    """
    user_id = token.get("sub")
    return {"message": f"Hello {user_id}"}
```

### Optional Auth

For endpoints that work with or without auth:

```python
from typing import Optional
from infrastructure.clerk_auth import get_optional_user

@app.get("/api/public-info")
async def public_info(user: Optional[dict] = Depends(get_optional_user)):
    if user:
        return {"message": f"Welcome back, {user.get('email')}"}
    return {"message": "Welcome, guest!"}
```

---

## Environment Variables Reference

### Frontend

| Variable | Required | Example |
|----------|----------|---------|
| `VITE_CLERK_PUBLISHABLE_KEY` | Yes (prod) | `pk_test_xxxx` |
| `VITE_API_URL` | Yes | `http://localhost:8000` |
| `VITE_SPECKLE_SERVER` | No | `https://app.speckle.systems` |

### Backend

| Variable | Required | Example |
|----------|----------|---------|
| `CLERK_DOMAIN` | Yes (if using auth) | `my-app.clerk.accounts.com` |
| `CLERK_FRONTEND_API_URL` | Yes (if using auth) | `http://localhost:5173` |

---

## Security Considerations

1. **Token Storage**: Clerk automatically uses httpOnly cookies when possible, preventing XSS token theft
2. **Token Validation**: Backend validates every token's signature using Clerk's public keys (JWKS)
3. **No Client Token Handling**: Users never manually provide tokens
4. **Key Rotation**: Clerk rotates keys automatically; backend caches JWKS for 1 hour
5. **CORS**: Frontend and backend communicate with proper CORS headers

---

## Troubleshooting

### "VITE_CLERK_PUBLISHABLE_KEY not configured"
- Check your `.env` file has the key
- Restart the dev server after updating `.env`

### "CLERK_DOMAIN not configured" (backend)
- Set `CLERK_DOMAIN` in backend `.env`
- Use format: `your-app.clerk.accounts.com` (not full URL)

### Tests Failing with Auth
If you have existing tests, they may need the `CLERK_DOMAIN` environment variable set for the test environment.

### "Failed to fetch Clerk JWKS"
- Check internet connectivity
- Verify `CLERK_DOMAIN` is correct
- Check that Clerk API is accessible

---

## File Changes Summary

### Created Files
- `frontend/src/config/clerk.js` - Clerk config
- `frontend/src/store/auth-clerk.js` - Auth helpers
- `frontend/src/views/SignIn.vue` - Sign-in page
- `frontend/src/views/SignUp.vue` - Sign-up page
- `backend/src/infrastructure/clerk_auth.py` - JWT validation

### Modified Files
- `frontend/src/main.js` - Added Clerk plugin
- `frontend/src/router/index.js` - Added auth guards and Clerk imports
- `frontend/src/components/layout/Header.vue` - Uses Clerk's UserButton
- `frontend/.env` - Added Clerk key variable
- `frontend/.env.production` - Added Clerk key variable
- `backend/src/main.py` - Added health check, example protected endpoint
- `backend/requirements.txt` - Added auth dependencies

### Deleted Files (Deprecated)
- `frontend/src/views/Login.vue` - Replaced by Clerk sign-in
- `frontend/src/store/auth.js` - Replaced by auth-clerk.js
- `frontend/src/components/layout/Avatar.vue` - Use Clerk's UserButton

---

## Next Steps

1. ✅ Create Clerk account and get keys
2. ✅ Update environment variables
3. ✅ Update API endpoints to use `@Depends(verify_clerk_token)`
4. ✅ Add frontend API calls with token header
5. ✅ Deploy to production with production Clerk keys
6. ⚠️ Remove Legacy Speckle Token

---

## References

- [Clerk Vue Documentation](https://clerk.com/docs/component-libraries/vue)
- [JWT/JWKS Verification](https://clerk.com/docs/backend-requests/handling/jwt-verification)
- [Clerk Environment Variables](https://clerk.com/docs/deployments/set-environment-variables)
