# Digital Tissue Backend

Python FastAPI backend for metric calculation and Speckle model analysis.

## Local Development

### Setup

1. Navigate to backend folder:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```
   Or with pip:
   ```bash
   pip install -e .
   ```

3. Configure authentication (Clerk JWT verification):
  ```bash
  # backend/.env
  CLERK_DOMAIN=your-app.clerk.accounts.dev
  CLERK_ISSUER=https://your-app.clerk.accounts.dev
  CLERK_FRONTEND_API_URL=http://localhost:5174  # Update to match your frontend port
  ALLOWED_EMAIL_DOMAIN=students.iaac.net
    CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:5174,https://elena-corio.github.io
    LOCAL_AUTH_OPTIONAL=true
    AUTH_FAILURE_WINDOW_SECONDS=300
    AUTH_FAILURE_MAX_ATTEMPTS=20
  ```

  ### Local Development (Auth Optional by Default)

  In local development (when `RENDER` is not set), protected endpoints accept missing `Authorization` headers and return a mock local user payload.

  > ⚠️ Common pitfall: if local auth is tightened (for example `LOCAL_AUTH_OPTIONAL=false`) while the frontend runs without Clerk tokens, API calls return `401` and the UI may appear as “no data from backend”.

  You can explicitly control this behavior with `LOCAL_AUTH_OPTIONAL`:
  - `LOCAL_AUTH_OPTIONAL=true` → allow missing auth header
  - `LOCAL_AUTH_OPTIONAL=false` → require auth header even locally

  To bypass all checks regardless of headers, set `SKIP_AUTH=true`.

### Running the Server

```bash
# Option 1: Using uvicorn directly (recommended for development)
python -m uvicorn asgi:app --reload

# Option 2: Running main.py directly
python src/main.py
```

This will:
- **Check cache**: Look for existing cached metrics in `backend/metrics_cache/`
- **Calculate if needed**: If cache is empty, fetch latest Speckle version and calculate all metrics
- **Start server**: Listen on `http://127.0.0.1:8000`

The server runs with auto-reload enabled for development (uvicorn) or without (main.py).

### Testing

```bash
pytest
```

Or from backend directory:
```bash
..\.venv\Scripts\pytest
```

All metrics have comprehensive unit test coverage (26+ tests).

## Architecture (Hexagonal/Clean)

```
backend/src/
├── main.py                    # FastAPI app entry point
├── config.py                  # Environment and configuration
├── domain/                    # Core business logic
│   ├── enum.py               # ProgramType enumeration
│   ├── model.py              # Domain models (Building, Unit, Room, MetricResult)
│   ├── metric.py             # MetricResult dataclass
│   ├── *.py                  # 8 metric calculation functions
│   ├── json/
│   │   ├── rulebook.json     # Scoring rules and distance ranges
│   │   └── metrics.json      # Metric definitions (names, formulas, benchmarks)
│   └── __init__.py
├── application/              # Use cases and orchestration
│   ├── metrics_service.py    # Metric calculation orchestration
│   ├── metrics_workflow.py   # High-level workflow (Speckle → calculate → save)
│   └── __init__.py
├── infrastructure/           # External services and storage
│   ├── metrics_storage.py    # JSON file persistence (cache management)
│   └── __init__.py
├── adapters/                 # External interfaces (API, Speckle, etc.)
│   ├── api/
│   │   └── metrics.py        # REST API endpoints
│   ├── speckle/
│   │   ├── get_client.py     # SpecklePy client initialization
│   │   ├── get_latest_version.py  # Fetch latest model version
│   │   ├── receive_data.py   # Download and deserialize model
│   │   ├── mappers.py        # Convert Speckle objects to domain models
│   │   └── __init__.py
│   └── __init__.py
└── __pycache__/
```

### Key Layers

**Domain (`domain/`)**: Core business logic
- 8 metric calculation functions (2 fully implemented, 6 scaffolded)
- Single-pass algorithms for efficient processing
- Rulebook-based scoring with distance ranges
- All calculations return `MetricResult` dataclass

**Application (`application/`)**: Orchestration
- `metrics_service.py`: Calculates all metrics for a model
- `metrics_workflow.py`: Speckle integration - fetch version → calculate → save

**Infrastructure (`infrastructure/`)**: Persistence
- JSON file storage in `backend/metrics_cache/{version_id}.json`
- Automatic 2-decimal rounding for metric values
- File modification time-based "latest" version detection

**Adapters (`adapters/`)**: External interfaces  
- FastAPI REST endpoints with enriched metric definitions
- Speckle client integration via SpecklePy
- Data mappers: Speckle objects → domain models

## Authentication & Authorization

- Clerk JWT validation is implemented in `src/infrastructure/clerk_auth.py`.
- All `/api/metrics` routes use `verify_clerk_token` and enforce access checks.
- Domain authorization is enforced through `ALLOWED_EMAIL_DOMAIN` (comma-separated list supported).
- Unauthorized domains return `403`.
- Auth failures are logged (missing header, malformed header, JWT failures, missing email claim, disallowed domain) without logging tokens.
- Repeated auth failures are rate-limited per client IP (`429 Too Many Requests`).

## API Endpoints

### GET `/api/metrics`
Fetch latest calculated metrics enriched with definitions.

**Response:**
```json
{
  "daylight_potential": {
    "name": "Daylight Potential",
    "formula": "window_area / net_floor_area",
    "benchmark": 0.25,
    "label": "Glazed facade area",
    "action": "The windows area...",
    "total_value": 0.42,
    "value_per_level": {...},
    "value_per_cluster": {...},
    "chart_data": {...}
  },
  ...
}
```

**Status Codes:**
- `200 OK`: Metrics found and returned
- `404 Not Found`: No cached metrics (run calculation first)

### GET `/api/metrics/{version_id}`
Fetch metrics for a specific Speckle version.

**Parameters:**
- `version_id` (string): Speckle version ID

**Response:** Same structure as `/api/metrics`

### GET `/api/metrics/history`
List all cached metric versions.

**Response:**
```json
{
  "message": "Found 2 cached versions",
  "versions": {
    "a55c8d5fa8": "/path/to/metrics_cache/a55c8d5fa8.json",
    "b66d9e6fb9": "/path/to/metrics_cache/b66d9e6fb9.json"
  }
}
```

### POST `/api/metrics/calculate`
Trigger metric calculation for the latest Speckle version.

*Endpoint exists but is not yet triggered automatically. Currently calculations are triggered on startup (Option C: check cache, calculate if empty).*

**Response:**
```json
{
  "message": "Metrics calculated successfully",
  "metrics": {...}  // Same structure as GET /api/metrics
}
```

**Future Use Case:** Will be called by Speckle webhook on version updates (deployment environment).

## Metrics System

### Fully Implemented (42 Tests)

**Daylight Potential** (`domain/daylight_potential.py`)
- Formula: `window_area / net_floor_area`
- Benchmark: 0.25
- Scoring: Distance-based ranges with interpolation

**Green Space Index** (`domain/green_space_index.py`)
- Formula: `residents_close_to_green_count / residents_count`
- Benchmark: 0.80
- Scoring: Proximity ranges (< 300m is good)

### Scaffolded (Ready for Implementation)

6 additional metrics with calculation stubs:
- Program Diversity Index
- Circulation Efficiency  
- Occupancy Efficiency
- Net Floor Area Ratio
- Envelope Efficiency
- Carbon Efficiency

All return `MetricResult` with metadata from `metrics.json`. Calculation logic TBD.

### Rulebook System

**Distance-based scoring** (`domain/json/rulebook.json`):
```json
{
  "proximity_ranges": {
    "max_gap": 8.0,
    "ranges": [
      {"min": 0, "max": 100, "score": 1.0},
      {"min": 100, "max": 300, "score": 0.8},
      ...
    ]
  }
}
```

**Metric definitions** (`domain/json/metrics.json`):
- `name`: Display name
- `benchmark`: Target value
- `formula`: Mathematical formula (for frontend display)
- `label`: Metric category
- `action`: Improvement recommendation

## Caching & Versioning

**Cache Location:** `backend/metrics_cache/{version_id}.json`

**Automatic Features:**
- ✅ 2-decimal rounding on save
- ✅ Latest version detection by modification time
- ✅ Version history available via API
- ✅ Smart startup: only calculate if cache empty

**Cache Format:**
```json
{
  "metric_slug": {
    "name": "...",
    "benchmark": 0.0,
    "total_value": 0.42,
    "value_per_level": {...},
    "value_per_cluster": {...},
    "chart_data": {...}
  }
}
```

## Dependencies

Key packages (see `pyproject.toml`):
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `specklepy` - Speckle client
- `pydantic` - Data validation
- `pytest` - Testing framework

## Deployment

### Local Development
```bash
python -m uvicorn asgi:app --reload
```
Or:
```bash
python src/main.py
```

### Render.com Production
Single command deployment:
```bash
python src/main.py
```

### GitHub Actions (Planned)
Auto-deploy to Render on push to main.

### Speckle Webhook (Planned)
Configure in Speckle dashboard:
- Event: `Project Version Created`
- URL: `https://your-render-url/api/metrics/calculate`
- Automatically recalculates metrics on new versions

*Currently the endpoint exists but webhook listener is not yet implemented.*

## Contributing

- Tests required for new metrics
- Follow hexagonal architecture layering
- Add metric definitions to `metrics.json` before implementation
- Keep `domain/` free of external dependencies
