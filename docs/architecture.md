# Digital Tissue Architecture (2026)

## System Overview

A full-stack computational design intelligence system combining Vue 3 frontend with Python FastAPI backend. The system fetches architectural models from Speckle, calculates performance metrics, and provides an interactive dashboard with KPI tracking.

**Tech Stack:**
- **Frontend**: Vue 3 + Vite, deployed to GitHub Pages
- **Backend**: Python FastAPI, deployed to Render.com
- **Data Source**: Speckle platform via SpecklePy client
- **Persistence**: JSON files (metrics_cache/)

## Architecture Layers

### Backend (Hexagonal/Clean Architecture)

```
domain/              Core business logic (metrics, calculations, rules)
├── model.py         Domain models (Building, Unit, MetricResult)
├── enum.py          ProgramType enumeration
├── metric.py        MetricResult dataclass
├── *.py             Metric calculation functions (8 total)
└── json/
    ├── rulebook.json    Distance-based scoring rules
    └── metrics.json     Metric definitions (names, formulas, benchmarks)

application/         Orchestration layer
├── metrics_service.py      Calculates all metrics for a model
└── metrics_workflow.py     High-level Speckle → Calculate → Save flow

infrastructure/      External integrations
└── metrics_storage.py      JSON file persistence and caching

adapters/            API and external interfaces
├── api/metrics.py       REST endpoints (GET, POST)
└── speckle/             Speckle integration
    ├── get_client.py
    ├── get_latest_version.py
    ├── receive_data.py
    └── mappers.py       Convert Speckle → Domain objects
```

**Key Design Principle**: Each layer is independent and testable. Domain has zero external dependencies.

### Frontend (Component-Based)

```
views/
├── Homepage.vue      Hero section with CTAs
├── About.vue         Feature cards
├── Login.vue         Authentication
└── Workspace.vue     Main container (Router outlet)
    └── workspace/
        ├── Viewer.vue       3D model viewer
        └── Metrics.vue      KPI dashboard

components/
├── cards/            Reusable card components
│   ├── TitleCard.vue     KPI header
│   ├── MetricCard.vue    Metric display
│   └── TextCard.vue      Text content
├── layout/           Global layout
│   ├── Header.vue        Navigation
│   └── Avatar.vue        User avatar
└── viewer/           Viewer controls
    ├── SpeckleViewer.vue
    ├── ViewerContent.vue
    ├── ButtonBar.vue
    ├── IconButton.vue
    └── PromptBar.vue

services/
└── metricsApi.js     Backend API communication

config/
├── uiText.js         ALL UI strings and KPI structure
├── modelConfig.js    Viewer configuration
└── router/index.js   Vue Router setup
```

**Key Design Principle**: Single responsibility, data-driven rendering, all text centralized.

## Data Flow

### Startup Flow (Option C)

```
User runs: python src/main.py
    ↓
Check if metrics cache exists
    ↓
├─ YES → Skip calculation, start server
└─ NO → Calculate metrics, save to cache, start server
    ↓
FastAPI server ready at http://localhost:8000
```

### Metric Calculation Flow

```
Speckle Project
    ↓
get_client() → SpecklePy client
    ↓
get_latest_version() → Fetch version ID
    ↓
receive_data() → Download and deserialize model
    ↓
mappers.py → Convert Speckle objects to Domain models
    ↓
metrics_service.calculate_all_metrics(model)
    ├── daylight_potential()
    ├── green_space_index()
    ├── program_diversity_index()
    ├── circulation_efficiency()
    ├── occupancy_efficiency()
    ├── net_floor_area_ratio()
    ├── envelope_efficiency()
    └── carbon_efficiency()
    ↓
metrics_storage.save_metrics(version_id, results)
    → backend/metrics_cache/{version_id}.json (rounded to 2 decimals)
```

### Frontend Data Flow

```
Frontend loads: http://localhost:5173
    ↓
Metrics.vue mounts
    ↓
fetchLatestMetrics() → GET http://localhost:8000/api/metrics
    ↓
Backend returns enriched metrics:
{
  "daylight_potential": {
    "name": "Daylight Potential",
    "formula": "window_area / net_floor_area",
    "benchmark": 0.25,
    "label": "Glazed facade area",
    "action": "Increase windows...",
    "total_value": 0.42,
    "value_per_level": {...},
    "value_per_cluster": {...}
  },
  ...
}
    ↓
matchMetricsToKPIs(uiText.kpis, backendMetrics)
    ↓ Converts metric slugs to objects:
{
  name: "Liveability",
  metrics: [
    {name: "Daylight Potential", value: 0.42, benchmark: 0.25, ...},
    {name: "Green Space Index", value: 0.54, benchmark: 0.80, ...}
  ]
}
    ↓
MetricCard components render with:
- Name (from backend)
- Value (rounded to 2 decimals)
- Benchmark (rounded to 2 decimals)
- Formula (from backend on hover)
```

## API Endpoints

**Base URL**: `http://localhost:8000/api/metrics`

| Endpoint | Method | Purpose | Response |
|----------|--------|---------|----------|
| `/api/metrics` | GET | Latest metrics (enriched) | 200 OK or 404 |
| `/api/metrics/{version_id}` | GET | Specific version | 200 OK or 404 |
| `/api/metrics/history` | GET | All cached versions | {message, versions} |
| `/api/metrics/calculate` | POST | Trigger calculation | {message, metrics} |

**Response Format** (enriched with definitions):
```json
{
  "metric_slug": {
    "name": "Display Name",
    "formula": "Mathematical formula",
    "benchmark": 0.75,
    "label": "Category label",
    "action": "Improvement recommendation",
    "total_value": 0.42,
    "value_per_level": {...},
    "value_per_cluster": {...},
    "chart_data": {...}
  }
}
```

## Caching Strategy

**Cache Directory**: `backend/metrics_cache/`

**File Format**: `{version_id}.json` (e.g., `a55c8d5fa8.json`)

**Features**:
- ✅ Automatic 2-decimal rounding on save
- ✅ Latest version detection by file modification time
- ✅ Version history available via API
- ✅ Smart startup: calculate only if cache is empty

**Cache Invalidation** (future):
- Manual: DELETE `/api/metrics/{version_id}`
- Automatic: On Speckle version update (webhook)

## KPI Structure

**4 KPI Categories** (from `config/uiText.js`):

1. **Liveability** - Capacity to support everyday wellbeing
   - Daylight Potential
   - Green Space Index

2. **Interconnection** - Connections between people and programs
   - Program Diversity Index
   - Circulation Efficiency

3. **Adaptability** - Capacity of spaces to transform
   - Occupancy Efficiency
   - Net Floor Area Ratio

4. **Sustainability** - Environmental performance
   - Envelope Efficiency
   - Carbon Efficiency

Each KPI is paired with 2 metrics. Display is organized in a 3-row grid:
- Row 1: KPI title cards
- Row 2: First metric per KPI
- Row 3: Second metric per KPI

## Metric Calculation System

**Rulebook-Based Scoring** (`domain/json/rulebook.json`):
- Distance ranges with interpolation
- Examples: proximity scoring (0-300m), efficiency thresholds

**Metric Definitions** (`domain/json/metrics.json`):
- Name, formula, benchmark per metric
- Label, action, and other metadata
- Provides UI text for frontend

**Implementation Status**:
- ✅ 2 fully implemented: Daylight Potential, Green Space Index
- 🔄 6 scaffolded: Need calculation logic implementation

## Deployment Strategy

**Local Development**:
```bash
# Terminal 1: Backend
cd backend
python src/main.py

# Terminal 2: Frontend
cd frontend
npm run dev
```

**Production**:
- **Frontend**: GitHub Pages (auto-deploy on push to main)
  - Base path: `/digital-tissue/`
  - Runs on: `https://elena-corio.github.io/digital-tissue`

- **Backend**: Render.com
  - Command: `python src/main.py`
  - Environment: Set `SPECKLE_TOKEN` and `PROJECT_ID`
  - Runs on: `https://your-render-backend.com`

**Webhook** *(planned)*:
- Speckle sends POST to `/api/metrics/calculate` on version updates
- Backend recalculates and caches new metrics
- Frontend refreshes to show latest values

## Design Principles

1. **No Hardcoded Text**: All strings in `config/uiText.js`
2. **DRY Components**: Data-driven rendering with `v-for`
3. **Type Safety**: Python type hints throughout backend
4. **Separation of Concerns**: Hexagonal architecture in backend
5. **Reusability**: Shared base components (cards, buttons)
6. **Testability**: 26+ unit tests, mocked Speckle data for testing

## Future Enhancements

1. **Metric Insights Tab**: Recommendations based on calculations
2. **Speckle Webhooks**: Auto-calculate on version updates
3. **Remaining 6 Metrics**: Full implementation with tests
4. **GraphQL Subscriptions**: Real-time model updates
5. **Database**: Persistent metrics history (Redis/PostgreSQL)
6. **User Authentication**: Proper login flow with Speckle OAuth

## File Structure Summary

```
digital-tissue/
├── README.md                    Overall guide
├── backend/
│   ├── README.md               Backend documentation
│   ├── pyproject.toml          Dependencies
│   ├── pytest.ini              Test configuration
│   └── src/
│       ├── main.py             FastAPI app + startup
│       ├── config.py           Environment config
│       ├── domain/             Business logic
│       ├── application/        Use cases
│       ├── infrastructure/     Storage
│       ├── adapters/           API & integrations
│       └── tests/              Unit tests
├── frontend/
│   ├── README.md               Frontend documentation
│   ├── package.json            Dependencies
│   ├── vite.config.js          Build config
│   ├── index.html              Entry page
│   └── src/
│       ├── main.js             Vue app entry
│       ├── App.vue             Root component
│       ├── components/         Reusable components
│       ├── views/              Page components
│       ├── services/           API layer
│       ├── config/             Configuration
│       ├── router/             Routing
│       ├── store/              State (Pinia)
│       └── assets/             Images, styles
├── api/                         API contracts
├── docs/                        Documentation
│   ├── architecture.md          This file
│   ├── design.md               UI/UX design
│   └── logs/prompts.md         Development log
└── metrics_cache/              Cached metrics (git-ignored)
```