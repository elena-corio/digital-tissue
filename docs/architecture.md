# Architecture

## Tech Stack

- **Vue 3** (Composition API) + **Vite 5** + **Vue Router 4**
- **CSS** with design tokens (no preprocessors)
- **GitHub Pages** deployment

## Project Structure

```
frontend/
├── index.html
├── vite.config.js
├── package.json
└── src/
    ├── main.js
    ├── App.vue
    ├── config/
    │   └── uiText.js           # All UI text + KPI data
    ├── router/
    │   └── index.js            # Nested routes for workspace
    ├── views/                  # Page components
    │   ├── Homepage.vue
    │   ├── Workspace.vue       # Parent with tab navigation
    │   ├── About.vue           # 4x2 card grid
    │   ├── Login.vue
    │   └── workspace/
    │       ├── Viewer.vue
    │       └── Metrics.vue     # 4-column KPI grid
    ├── components/
    │   ├── layout/
    │   │   └── Header.vue
    │   ├── navigation/
    │   └── cards/
    │       ├── TitleCard.vue   # Icon + name + description
    │       ├── TextCard.vue    # Bullet list with fuchsia dots
    │       └── MetricCard.vue  # Value/benchmark + formula tooltip
    └── assets/
        ├── images/
        │   ├── logo.svg
        │   └── icons/
        └── styles/
            ├── colors.css
            ├── typography.css
            └── globals.css     # .card base, .btn variants
```

## Data Flow

All UI text comes from `uiText.js`:

```javascript
// config/uiText.js
export const uiText = {
  app: { title: 'Digital Tissue' },
  navigation: { home: 'Home'}
}
```

Components import and use it:

```vue
<script setup>
import { uiText } from '@/config/uiText.js'
</script>
<template>
  <h1>{{ uiText.app.title }}</h1>
</template>
```

**Why:** Single source of truth, no hard-coded text, easy to translate later.

**KPI Data Structure:**

KPIs stored in `uiText.kpis` with nested metrics:

```javascript
kpis: {
  kpi1: {
    name: 'Liveability',
    description: 'Capacity to support everyday wellbeing',
    icon: 'livable.svg',
    metrics: [
      {name: 'Service Density Index', formula: '...', benchmark: '0.05', value: '0.04'},
      {name: 'Urban Green Space', formula: '...', benchmark: '1.00', value: '0.80'}
    ]
  }
}
```

Components iterate with `v-for` over kpis and nested metrics for DRY code.

## Navigation

**Router (nested routes):**
- `/` → Homepage (hero with CTA buttons)
- `/about` → About (4x2 card grid with for loops)
- `/workspace` → Workspace (redirects to `/workspace/viewer`)
  - `/workspace/viewer` → Viewer tab (placeholder)
  - `/workspace/metrics` → Metrics tab (4-column KPI grid)
- `/login` → Login

**Tab Navigation:** Workspace uses Vue Router nested routes with `<router-link>` tabs and `<router-view>` outlet. Active tab styled with fuchsia underline.

## Deployment

**Development:**
```bash
npm run dev  # Runs at localhost:5173
```

**Production:**
```bash
npm run build  # Outputs to frontend/dist/
```

**Environment-aware base path:**
- Dev: `base: '/'`
- Production: `base: '/digital-tissue/'` (for GitHub Pages)

## Design System

CSS custom properties in `/assets/styles/`:
- `colors.css` - Custom palette (navy-blue, fuchsia, light-lila, etc.)
- `typography.css` - Inter font, type scale, weights, line heights
- `globals.css` - Resets, `.card` base class, `.btn` system, shadows, spacing

**Shared Base Classes:**
- `.card` - Base for all card components (background, radius, shadow, hover)
- `.btn` + `.btn-primary/secondary/tertiary` - Global button system

**Asset Handling:** Dynamic imports using `new URL('../../assets/path', import.meta.url).href` for GitHub Pages compatibility.

**Component Patterns:** For loops (`v-for`) to iterate over `uiText.cards` and `uiText.kpis` for DRY code.

## Key Decisions

| Decision | Why |
|----------|-----|
| Vue 3 Composition API | Better code organization, reusability |
| Vite | Faster dev server, simpler config |
| CSS variables | No build step, runtime theming |
| Config-based UI text + data | Centralized, i18n-ready, mock data in uiText.js |
| Vue Router nested routes | Professional workspace tabs with shareable URLs |
| Shared base classes (.card, .btn) | Consistent styling, single source of truth |
| For loops in views | DRY code, easier to maintain |
| Dynamic asset imports | GitHub Pages base path compatibility |
| Monorepo | Future backend integration |

## Speckle Viewer Architecture

### Workspace Viewer
- The Workspace view integrates Speckle model visualization for BIM/geometry data.
- Two viewer panels, each with a PromptBar for model ID input and a SpeckleViewer component.
- Project ID is sourced from `/src/config/modelConfig.js` and remains fixed.
- Model ID defaults from config but can be updated live via the prompt input.
- When a new model ID is entered and updated, the viewer reloads the model using Vue's reactivity and a key binding.

### Data & Config
- Speckle authentication token and server URL are set in `.env` as `VITE_SPECKLE_TOKEN` and `VITE_SPECKLE_SERVER`.
- `modelConfig.js` stores project and model IDs for each viewer panel.

### Component Communication
- PromptBar emits update events to parent (Viewer.vue) to trigger model reload.
- Viewer.vue manages model ID state and passes updated URLs to SpeckleViewer.
- SpeckleViewer re-mounts on URL change, ensuring model reload.

### User Flow
1. User sees default model loaded from config.
2. User enters a new model ID in PromptBar and clicks update.
3. Viewer reloads with new model, keeping project ID fixed.

### Security & Environment
- Sensitive tokens are never hard-coded; always stored in `.env`.
- Model/project IDs are mock data in config for easy testing and future backend integration.

### Extensibility
- Ready for backend integration (monorepo structure).
- UI text and KPI data are centralized for easy translation and mock data swapping.
