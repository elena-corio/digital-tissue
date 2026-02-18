# Digital Tissue

A living data system for design intelligence. This monorepo contains both the frontend (Vue 3 + Vite) and backend (Python FastAPI) applications, along with documentation and shared API contracts.

## Monorepo Structure

```
digital-tissue/
├── frontend/       # Vue 3 + Vite application (see frontend/README.md)
├── backend/        # Python FastAPI backend (see backend/README.md)
├── api/            # API contracts and client samples
├── docs/           # Project documentation
└── metrics_cache/  # Cached metric calculations (JSON files)
```

## Getting Started

### Quick Setup

**Backend** (Terminal 1):
```bash
cd backend
..\.venv\Scripts\python.exe src/main.py
```

Or, if you are already in the backend directory:

```bash
.venv\Scripts\python.exe src/main.py
```

This will:
- Check if metrics are cached
- Calculate metrics if cache is empty  
- Start server on `http://localhost:8000`

**Frontend** (Terminal 2):
```bash
cd frontend
npm run dev
```
Opens app at `http://localhost:5173`

For detailed instructions, see individual README files:

- [frontend/README.md](frontend/README.md)
- [backend/README.md](backend/README.md)

## Running the backend locally

From the project root, run:

```
cd backend
..\.venv\Scripts\python.exe src/main.py
```

Or, if you are already in the backend directory:

```
.venv\Scripts\python.exe src/main.py
```

## Data Flow

1. **Backend** (FastAPI):
   - Fetches Speckle model data via SpecklePy client
   - Calculates metrics based on model geometry and rulebook
   - Exposes REST API: `/api/metrics`, `/api/metrics/{version_id}`, `/api/metrics/history`
   - Enriches metrics with definitions from `metrics.json`
   - Caches results in `backend/metrics_cache/{version_id}.json`

2. **Frontend** (Vue 3):
   - Fetches metrics from backend `/api/metrics`
   - Maps metric slugs to KPI categories (Liveability, Interconnection, Adaptability, Sustainability)
   - Displays metrics with names, benchmarks, formulas, and calculated values
   - All text from `config/uiText.js` - no hardcoded strings

## Metrics System

**8 Calculated Metrics:**
- Daylight Potential (glazed facade area)
- Green Space Index (proximity to green)
- Program Diversity Index (program mix)
- Circulation Efficiency (efficient circulation)
- Occupancy Efficiency (usable area ratio)
- Net Floor Area Ratio (net-to-gross floor area)
- Envelope Efficiency (envelope components)
- Carbon Efficiency (embodied carbon impact)

**Scoring**: Rulebook-based with distance ranges and benchmark thresholds defined in `domain/json/rulebook.json` and `domain/json/metrics.json`

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/metrics` | GET | Latest calculated metrics (enriched with definitions) |
| `/api/metrics/{version_id}` | GET | Specific version metrics |
| `/api/metrics/history` | GET | List all cached metric versions |
| `/api/metrics/calculate` | POST | Trigger metric calculation for latest Speckle version |

## Deployment

- **Frontend**: GitHub Pages (automatic via GitHub Actions on push to main)
- **Backend**: Render.com (single command: `python src/main.py`)
- **Webhook** *(planned)*: POST to `/api/metrics/calculate` to trigger calculation on Speckle version updates

## Documentation

For detailed documentation, see the [docs/](docs/) folder.

## Contributing

Please see the individual frontend and backend README files for contribution guidelines and development workflow.


## Clerk Security Best Practices

1. **Never put secret keys in client-side code**
   - Only use Clerk publishable keys in frontend code.
   - Never expose `CLERK_SECRET_KEY`, `CLERK_JWT_KEY`, or any backend API keys in the browser.

2. **Use Clerk’s server helpers for backend logic**
   - Always validate Clerk tokens on the backend using official libraries or your own secure validation logic.

3. **Do NOT pass backend tokens to the frontend**
   - Only pass frontend-scoped, short-lived tokens to the browser.
   - Never expose backend secrets or long-lived tokens in client-side code.

4. **Use secure HTTP-only cookies for session tokens (optional)**
   - For extra security, consider using HTTP-only cookies for session tokens so they are not accessible via JavaScript.

5. **If you’re using a custom backend, issue your own API tokens**
   - If your backend needs to issue tokens, generate and validate them securely, and never expose signing keys to the frontend.
