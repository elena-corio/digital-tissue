# Digital Tissue Frontend

A Vue 3 + Vite application for computational design dashboards and Speckle model visualization.

## Quick Start

```bash
cd frontend
npm install
npm run dev
```
The app will open at http://localhost:5173

Build for production:
```bash
npm run build
```
Preview production build:
```bash
npm run preview
```

## Features

- Global Header with navigation and login
- Homepage with hero section and CTAs
- About page with feature cards
- Workspace with Viewer and Metrics tabs
- Metrics dashboard with interactive KPI cards
- Reusable card components and design system

## Architecture Principles

- No hard-coded UI text: all strings in `/src/config/uiText.js`
- Composable, single-responsibility Vue components
- Nested routing with Vue Router 4
- CSS design tokens for colors, spacing, shadows, typography
- Shared base classes for cards and buttons
- Dynamic asset imports (GitHub Pages compatible)
- DRY code: data-driven rendering

## Deployment

Automatic deployment to GitHub Pages via GitHub Actions:
- Trigger: Push to `main` branch
- Workflow: `.github/workflows/deploy.yml`
- Build: Runs `npm ci` and `npm run build` in frontend directory
- Deploy: Uploads `frontend/dist` to GitHub Pages

Base path configuration in `vite.config.js`:
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
