
# Digital Tissue Architecture (2026)

## Overview
Monorepo with a Vue 3 + Vite frontend and a FastAPI backend. All UI text and KPI data are centralized in the frontend config for easy translation and mock data swapping. The system is ready for backend integration and future expansion.

## Structure
- **frontend/**: Vue 3 app, Vite, design tokens, all UI text in config/uiText.js
- **backend/**: FastAPI, hexagonal architecture, REST API for metrics
- **api/**: (optional) for shared contracts or client code

## Data Flow
- Frontend fetches metrics from backend `/metrics` endpoint
- All UI text and KPI structure in `uiText.js`
- DRY code: components use `v-for` to render cards and metrics

## Navigation
- `/` Homepage (hero, CTA)
- `/about` About (feature cards)
- `/workspace` Workspace (tabs: Viewer, Metrics)
- `/login` Login

## Deployment
- Dev: `npm run dev` (localhost:5173)
- Prod: `npm run build` (GitHub Pages, base: '/digital-tissue/')

## Design & Decisions
- CSS variables for colors, spacing, typography
- Shared base classes: `.card`, `.btn`
- Dynamic asset imports for GitHub Pages compatibility
- Monorepo for future backend/frontend integration

## Speckle Integration
- Workspace view: two Speckle viewers, PromptBar for model ID
- Model/project IDs and tokens in config and .env
- Ready for real data and backend expansion
