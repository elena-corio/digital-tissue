# Design System

## Color Palette

### Primary & Accent Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--navy-blue-100` | #303179 | Primary brand, headers |
| `--blue-100` | #3b479f | Structure |
| `--light-blue-100` | #4697e3 | Facade |
| `--fucsia-100` | #e9268c | Data |
| `--orange-100` | #e7882f | Program |
| `--yellow-100` | #f0b43a | Circulation |

### Neutral Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--light-lila-100` | #d8d9ed | Cards |
| `--light-grey-100` | #dadad9 | Button |

### Semantic Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--color-success` | #10b981 | Success states |
| `--color-warning` | #f59e0b | Warnings |
| `--color-error` | #ef4444 | Errors |
| `--color-info` | #3b82f6 | Info messages |

## Typography

**Font:** Inter

### Type Scale

| Token | Size | Usage |
|-------|------|-------|
| `--font-size-h1` | 2.4rem | Hero titles |
| `--font-size-h2` | 1.6rem | Page titles |
| `--font-size-h3` | 1.2rem | Section headers |
| `--font-size-body` | 1rem | Body text |
| `--font-size-small` | 0.875rem | Secondary text |
| `--font-size-caption` | 0.75rem | Labels |

### Weights

- `--font-weight-regular`: 400 (body text)
- `--font-weight-medium`: 500 (navigation, buttons)
- `--font-weight-semibold`: 600 (card titles)
- `--font-weight-bold`: 700 (headings)

### Line Heights

- `--line-height-tight`: 1.1 (large headings)
- `--line-height-normal`: 1.4 (UI elements)
- `--line-height-relaxed`: 1.6 (long content)

## Spacing

```css
--space-sm: 0.5rem;    /* 8px - tight spacing */
--space-md: 1rem;      /* 16px - standard */
--space-lg: 2rem;      /* 32px - sections */
--space-xl: 3rem;      /* 48px - large sections */
```

## Border Radius

```css
--radius-small: 4px;   /* Buttons, inputs */
--radius-medium: 8px;  /* Cards */
--radius-large: 12px;  /* Modals, panels */
```

## Shadows

```css
--shadow-md: 0 2px 4px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 4px 8px rgba(0, 0, 0, 0.15);
--shadow-around-md: 0 0 8px rgba(0, 0, 0, 0.1);
--shadow-around-lg: 0 0 16px rgba(0, 0, 0, 0.15);
```

## Design Principles

1. **Use design tokens** - Always reference CSS variables, never hard-code values
2. **Single responsibility** - Components do one thing well
3. **Composition over complexity** - Combine simple components
4. **No hard-coded text** - All strings from `uiText.js`
5. **Shared base styles** - Use `.card` and `.btn` base classes for consistency
6. **Mobile-first** - Responsive by default

## Component Library

| Component | Purpose | Status |
|-----------|---------|--------|
| Header | Global header with logo, title, Login button | ✅ Built |
| Button | Action trigger (.btn base with primary/secondary/tertiary) | ✅ Built |
| TitleCard | Feature card with icon, name, description | ✅ Built |
| TextCard | Content card with bullet list (fuchsia dots) | ✅ Built |
| MetricCard | KPI metric with value/benchmark, formula tooltip | ✅ Built |
| TabNav | Workspace tab navigation | ✅ Built |

## Card System

All cards inherit from `.card` base class in `globals.css`:

# Digital Tissue Design System (2026)

## Colors & Typography
- Brand: navy-blue, fuchsia, light-lila, orange, yellow
- Font: Inter, with type scale and weights via CSS variables

## Spacing & Layout
- Spacing tokens: --space-sm/md/lg/xl
- Border radius: --radius-small/medium/large
- Shadows: --shadow-md/lg/around

## Principles
- Use design tokens (CSS variables) everywhere
- No hard-coded text: all UI strings in config
- Shared base classes: .card, .btn
- Mobile-first, responsive by default

## Components
- Header, Button, TitleCard, TextCard, MetricCard, TabNav (all built)
- All cards inherit from .card base class

## Card Types
- TitleCard: icon, name, description (light lila)
- TextCard: bullet list (fuchsia dots)
- MetricCard: metric name/value, formula tooltip

## Speckle Viewer
- Two-panel layout, PromptBar for model ID, SpeckleViewer for BIM/geometry
- Configurable via .env and modelConfig.js
- Keyboard accessible, responsive

