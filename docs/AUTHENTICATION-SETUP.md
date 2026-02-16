# Authentication Setup (Clerk JS)

This project uses Clerk JS (not the Vue plugin) and a custom composable to manage auth state and tokens.

## 1) Clerk account

- Create an app in the Clerk dashboard.
- Copy the **Publishable Key** (must start with `pk_test_` or `pk_live_`).

## 2) Frontend env

`frontend/.env` (local development)
```env
VITE_SPECKLE_SERVER=https://app.speckle.systems
VITE_API_URL=http://localhost:8000
VITE_CLERK_PUBLISHABLE_KEY=pk_test_YOUR_KEY_HERE
VITE_SKIP_AUTH=true  # Skip Clerk auth for local testing
```

`frontend/.env.production`
```env
VITE_API_URL=https://digital-tissue.onrender.com
VITE_CLERK_PUBLISHABLE_KEY=pk_live_YOUR_KEY_HERE
# No VITE_SKIP_AUTH - production requires authentication
```

## 3) Backend env

`backend/.env`
```env
CLERK_DOMAIN=your-app.clerk.accounts.dev
CLERK_ISSUER=https://your-app.clerk.accounts.dev
CLERK_FRONTEND_API_URL=http://localhost:5174  # Update to match your frontend port
ALLOWED_EMAIL_DOMAIN=students.iaac.net
# SKIP_AUTH not set - authentication is optional in local dev, required in production
```

## 4) Run locally

Frontend:
```bash
cd frontend
npm run dev
```

Backend:
```bash
cd backend
python src/main.py
```

## 5) Authentication behavior

### Local Development (`VITE_SKIP_AUTH=true`)
- **Frontend**: No authentication required, direct access to all routes
- **Backend**: No Authorization header needed, mock tokens returned
- **Purpose**: Easy testing without Clerk setup

### Production (no `VITE_SKIP_AUTH`)
- **Frontend**: Clerk JS required, must sign in to access `/workspace`
- **Backend**: All `/api/metrics` endpoints require valid Clerk JWT
- **Restriction**: Non-`@students.iaac.net` users receive `403 Forbidden`
- **Security**: Full JWT validation with audience/issuer checks

## 6) Key files

- `frontend/src/composables/useClerk.js` - Clerk initialization and session management
- `frontend/src/services/metricsApi.js` - Auth header building with dev mode bypass
- `frontend/src/router/index.js` - Route protection with `VITE_SKIP_AUTH` check
- `frontend/src/views/SignIn.vue` - Sign in page
- `frontend/src/views/SignUp.vue` - Sign up page
- `backend/src/infrastructure/clerk_auth.py` - JWT verification with local dev fallback
