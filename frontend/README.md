# Digital Tissue Frontend

Vue 3 + Vite application for computational design dashboards and Speckle model visualization.

## Quick Start

```bash
cd frontend
npm install
npm run dev
```

The app will open at `http://localhost:5173`. 

Make sure the **backend is running first** (`python src/main.py` from `/backend` folder) so the frontend can fetch metrics from `http://localhost:8000/api/metrics`.

## Development Commands

Build for production:
```bash
npm run build
```

Preview production build:
```bash
npm run preview
```

## Architecture

```
frontend/src/
├── main.js                 # App entry point
├── App.vue                 # Root component
├── components/
│   ├── cards/
│   │   ├── MetricCard.vue      # Display metric with value vs benchmark
│   │   ├── TextCard.vue        # Display text/bullet information
│   │   └── TitleCard.vue       # Display KPI title and description
│   ├── layout/
│   │   ├── Avatar.vue          # User avatar
│   │   └── Header.vue          # Global navigation header
│   ├── navigation/
│   └── viewer/
│       ├── SpeckleViewer.vue   # 3D model viewer wrapper
│       ├── ViewerContent.vue   # Viewer container with controls
│       ├── ButtonBar.vue       # Control buttons
│       ├── IconButton.vue      # Reusable icon button
│       └── PromptBar.vue       # Model ID input
├── views/
│   ├── About.vue           # Feature cards and info
│   ├── Homepage.vue        # Hero section and CTAs
│   ├── Login.vue           # Authentication
│   ├── Workspace.vue       # Main workspace layout
│   └── workspace/
│       ├── Metrics.vue     # Metrics dashboard (main feature)
│       └── Viewer.vue      # 3D model viewer
├── router/
│   └── index.js            # Vue Router configuration
├── store/
│   └── auth.js             # Authentication state (Pinia)
├── services/
│   └── metricsApi.js       # Backend API communication
├── config/
│   ├── modelConfig.js      # Model viewer configuration
│   └── uiText.js           # ALL UI text (no hardcoded strings)
├── assets/
│   ├── images/
│   │   └── icons/          # SVG icons and image assets
│   └── styles/
│       ├── colors.css      # Color design tokens
│       ├── globals.css     # Global styles
│       ├── typography.css  # Font scales
│       └── variables.css   # CSS custom properties
└── vite.config.js          # Vite configuration
```

## Key Features

### No Hardcoded Strings
All UI text lives in `src/config/uiText.js`:
- Navigation labels
- Page titles and descriptions
- KPI names and descriptions
- Error messages
- Common button labels

Update text in one place; changes propagate everywhere.

### Metrics Dashboard (Metrics.vue)

**Flow:**
1. Component mounts → calls `fetchLatestMetrics()` from backend
2. Backend returns metrics keyed by slug: `{ "daylight_potential": {...}, ...}`
3. `matchMetricsToKPIs()` maps metric slugs to KPI categories:
   - **Liveability**: Daylight Potential, Green Space Index
   - **Interconnection**: Program Diversity, Circulation Efficiency
   - **Adaptability**: Occupancy Efficiency, Net Floor Area Ratio
   - **Sustainability**: Envelope Efficiency, Carbon Efficiency
4. Displays in 3-row grid:
   - Row 1: KPI title cards
   - Row 2: First metric per KPI
   - Row 3: Second metric per KPI

**Metric Display:**
- Name (from backend)
- Formula (from backend)
- Benchmark value (rounded to 2 decimals)
- Calculated value (rounded to 2 decimals)
- Tooltip with formula on hover
- Color coding: green if ≥ benchmark, gray if below

### Backend Integration

**Service:** `src/services/metricsApi.js`
- `fetchLatestMetrics()` - GET `/api/metrics`
- `fetchMetricsByVersion(versionId)` - GET `/api/metrics/{version_id}`
- `listMetricVersions()` - GET `/api/metrics/history`
- `matchMetricsToKPIs(kpis, backendMetrics)` - Maps slugs to objects

**Error Handling:**
- 404 responses: "Metrics not available. Please calculate metrics first."
- Network errors: Logged with full context
- Missing metrics: Warning logged, graceful fallback

### Design System

**CSS Variables** (`variables.css`):
- Spacing scale: `--space-xs` to `--space-xl`
- Shadows: `--shadow-sm`, `--shadow-md`, `--shadow-lg`
- Border radius: `--radius-sm`, `--radius-md`
- Transitions: `--transition-fast`, `--transition-default`

**Color Tokens** (`colors.css`):
- Primary, secondary, accent colors
- Semantic colors: success, warning, error
- Gray scale for neutral elements
- Dark mode support ready

**Typography** (`typography.css`):
- Heading scales (h1-h6)
- Body text sizes
- Font weights and line heights

### Component Patterns

**Card Components:**
- `<TitleCard>` - KPI header card
- `<MetricCard>` - Metric display with value vs benchmark
- `<TextCard>` - Text and bullet content

All cards are responsive grid items with consistent styling.

**Reusable Elements:**
- `<IconButton>` - Icon with tooltip
- `<Avatar>` - User avatar display
- `<Header>` - Global navigation

## Deployment

### GitHub Pages

Automatic deployment via GitHub Actions:
1. Push code to `main` branch
2. GitHub Actions runs workflow in `.github/workflows/deploy.yml`:
   - Installs dependencies: `npm ci`
   - Builds project: `npm run build`
   - Uploads `frontend/dist` to GitHub Pages
3. Live at: `https://elena-corio.github.io`

**Configuration:**
- Base path in `vite.config.js`: `/digital-tissue/`
- Assets use dynamic imports for GitHub Pages compatibility

### Environment Variables

**Development** (`.env.local`):
```
VITE_API_URL=http://localhost:8000
```

**Production** (set in deployment):
```
VITE_API_URL=https://your-render-backend-url
```

## Testing

Component testing setup ready (test files not yet written):
```bash
npm run test
```

## Contributing

**Guidelines:**
- Add UI text to `uiText.js` before creating components
- Keep components single-responsibility
- Use design tokens from CSS variables
- Make components data-driven when possible
- Prefer Vue 3 `<script setup>` syntax
- Use Pinia for complex state (auth) but local `ref()` for UI state

**Code Organization:**
- `components/` - Reusable UI components
- `views/` - Page-level containers
- `services/` - API and business logic
- `store/` - Global state (Pinia)
- `config/` - Configuration and constants
- Development: `base: '/'`
- Production: `base: '/digital-tissue/'`

Manual deployment:
1. Run `npm run build` from the frontend directory
2. Deploy the `frontend/dist` folder to GitHub Pages

Setup requirements:
- Enable GitHub Pages in repository settings
- Set source to "GitHub Actions"

## Speckle Viewer Integration

- Workspace Viewer displays Speckle models by project and model ID
- Project ID is set in `/src/config/modelConfig.js`
- Model ID defaults from config, can be updated live in the Viewer
- When a new model ID is entered, the viewer reloads the model
- Speckle authentication token and server URL are set in `.env` as `VITE_SPECKLE_TOKEN` and `VITE_SPECKLE_SERVER`

### Example `.env` file

```
VITE_SPECKLE_TOKEN=<your-token>
VITE_SPECKLE_SERVER=https://app.speckle.systems
```

### Example `modelConfig.js`

```
export const viewerModels = [
  {
    projectId: 'dcca94731b',
    modelId: '12eeb8c918',
  },
  {
    projectId: 'dcca94731b',
    modelId: '854375e166',
  }
];
```

### Usage
- Start the frontend as usual
- In Workspace Viewer, enter a new model ID and click update to reload the viewer
- Project ID remains fixed from config
