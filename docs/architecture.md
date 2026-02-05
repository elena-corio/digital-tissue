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
    │   └── uiText.js           # All UI text centralized
    ├── router/
    │   └── index.js            # 5 routes
    ├── views/                  # Page components
    │   ├── Homepage.vue
    │   ├── Workspace.vue
    │   ├── About.vue
    │   └── Login.vue
    ├── components/
    │   ├── layout/
    │   └── navigation/
    └── assets/
        └── styles/
            ├── colors.css
            ├── typography.css
            └── globals.css
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

## Navigation

**Router (4 routes):**
- `/` → Homepage
- `/workspace` → Workspace
- `/about` → About
- `/login` → Login

**Tab Navigation:** Workspace view uses internal tabs (no route changes).

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
- `colors.css` - Custom palette + semantic colors
- `typography.css` - Inter font, type scale
- `globals.css` - Resets and global styles

## Key Decisions

| Decision | Why |
|----------|-----|
| Vue 3 Composition API | Better code organization, reusability |
| Vite | Faster dev server, simpler config |
| CSS variables | No build step, runtime theming |
| Config-based UI text | Centralized, i18n-ready |
| Monorepo | Future backend integration |
