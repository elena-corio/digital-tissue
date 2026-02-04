# Digital Tissue

Computational design dashboard built with Vue 3 + Vite.

## Monorepo Structure

```
digital-tissue/
├── frontend/          Vue 3 + Vite application
│   ├── src/
│   │   ├── config/    UI text configuration
│   │   ├── components/
│   │   │   ├── layout/
│   │   │   └── navigation/
│   │   ├── views/     Page components
│   │   ├── router/    Vue Router setup
│   │   └── assets/    Styles and static files
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
- **Clean routing**: Vue Router with dynamic base path for deployment flexibility
- **Design tokens**: CSS variables for consistent theming
- **Monorepo ready**: Prepared for future backend integration

## Technology Stack

- **Framework**: Vue 3 (Composition API)
- **Build Tool**: Vite 5
- **Routing**: Vue Router 4
- **Styling**: CSS with design tokens (no preprocessor)
- **Deployment**: GitHub Pages compatible

## Deployment

This project is configured for GitHub Pages deployment with environment-aware base paths:
- Development: `base: '/'`
- Production: `base: '/digital-tissue/'`

To deploy:
1. Run `npm run build` from the frontend directory
2. Deploy the `frontend/dist` folder to GitHub Pages

## Development

Current branch: `frontend-framework`

For detailed documentation, see `/docs`
