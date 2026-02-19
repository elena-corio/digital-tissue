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
python src/main.py
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

## Authentication

Clerk authentication is used for sign-in/sign-up. The backend validates Clerk JWTs for protected endpoints. All environment variables and secrets are managed in `env` and `env.production` files. No email domain filtering is enforced.

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
