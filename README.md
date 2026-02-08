# Digital Tissue

A living data system for design intelligence. Computational design dashboard built with Vue 3 + Vite.

## Features

- **Global Header**: Logo and navigation with Login button
- **Homepage**: Centered hero section with CTA buttons
- **About Page**: 4x2 grid of feature cards (Framework, Automation, Monitoring, Coordination)
- **Workspace**: Tabbed interface with Viewer and Metrics views
- **Metrics Dashboard**: 4-column KPI grid with interactive metric cards showing values, benchmarks, and formulas
- **Card Components**: Reusable TitleCard, TextCard, and MetricCard components with shared base styling
- **Design System**: Global CSS tokens for colors, spacing, shadows, typography, buttons, and cards

## Monorepo Structure

```
digital-tissue/
├── frontend/          Vue 3 + Vite application
│   ├── src/
│   │   ├── config/    UI text configuration
│   │   ├── components/
│   │   │   ├── layout/      Header component
│   │   │   ├── navigation/
│   │   │   └── cards/       TitleCard, TextCard, MetricCard
│   │   ├── views/           Page components
│   │   │   ├── workspace/   Viewer, Metrics
│   │   │   ├── Homepage.vue
│   │   │   ├── About.vue
│   │   │   ├── Workspace.vue
│   │   │   └── Login.vue
│   │   ├── router/          Vue Router with nested routes
│   │   └── assets/          Styles, images, icons
│   │       ├── styles/      colors, typography, globals (with .card base class)
│   │       └── images/
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
├── backend/           (Coming soon)
└── docs/              Project documentation
```

## Getting Started

### Frontend Development

Navigate to the frontend directory:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Run development server:
```bash
npm run dev
```

The app will open at `http://localhost:5173`

Build for production:
```bash
npm run build
```

Preview production build:
```bash
npm run preview
```

## Architecture Principles

- **No hard-coded UI text**: All strings externalized in `/src/config/uiText.js`
- **Composable components**: Reusable, single-responsibility Vue components
- **Nested routing**: Vue Router 4 with child routes for workspace tabs
- **Design tokens**: CSS variables for colors, spacing, shadows, typography
- **Global styling system**: Shared `.card` base class and `.btn` variants for consistency
- **Dynamic asset imports**: GitHub Pages compatible using `new URL()` pattern
- **DRY code**: For loops in views to iterate over data structures
- **Monorepo ready**: Prepared for future backend integration

## Technology Stack

- **Framework**: Vue 3 (Composition API)
- **Build Tool**: Vite 5
- **Routing**: Vue Router 4
- **Styling**: CSS with design tokens (no preprocessor)
- **Deployment**: GitHub Pages compatible

## Deployment

Automatic deployment to GitHub Pages via GitHub Actions:
- **Trigger**: Push to `main` branch
- **Workflow**: `.github/workflows/deploy.yml`
- **Build**: Runs `npm ci` and `npm run build` in frontend directory
- **Deploy**: Uploads `frontend/dist` to GitHub Pages

Base path configuration in `vite.config.js`:
- Development: `base: '/'`
- Production: `base: '/digital-tissue/'`

**Manual deployment:**
1. Run `npm run build` from the frontend directory
2. Deploy the `frontend/dist` folder to GitHub Pages

**Setup requirements:**
- Enable GitHub Pages in repository settings
- Set source to "GitHub Actions"

## Development

**Current branch**: `metrics-cards`

**Branch structure:**
- `main`: Production-ready code
- `feature/first-components`: Initial components (Header, cards, About page)
- `workspace-framework`: Workspace with tabbed navigation
- `metrics-cards`: Metrics dashboard with KPI cards (active)

For detailed documentation, see `/docs`

## Speckle Viewer Integration

- The Workspace Viewer allows users to view Speckle models by project and model ID.
- Project ID is set from `/src/config/modelConfig.js`.
- Model ID defaults from config, but can be updated live via the prompt input in the Viewer.
- When a new model ID is entered and updated, the viewer reloads the model.
- Speckle authentication token and server URL are set in `.env` as `VITE_SPECKLE_TOKEN` and `VITE_SPECKLE_SERVER`.

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
- Start the frontend as usual.
- In Workspace Viewer, enter a new model ID in the prompt and click update to reload the viewer with the new model.
- Project ID remains fixed from config.
