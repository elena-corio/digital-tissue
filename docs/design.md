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

```css
.card {
  background: white;
  border-radius: var(--radius-medium);
  box-shadow: var(--shadow-md);
  transition: box-shadow 0.2s ease;
}

.card:hover {
  box-shadow: var(--shadow-lg);
}
```

**Card Types:**
- **TitleCard**: Light lila background, centered icon/text, hover darkens background
- **TextCard**: White background, fuchsia bullet points, centered list
- **MetricCard**: White background, centered metric name/value, info icon with formula tooltip

## Speckle Viewer Design

### Workspace Viewer
- The Workspace view features a Speckle model viewer for real-time BIM/geometry visualization.
- Viewer layout uses two side-by-side panels, each with a PromptBar for model ID input and a SpeckleViewer component.
- Project ID is fixed from config; model ID defaults from config but can be updated live via the prompt input.
- When a new model ID is entered and updated, the viewer reloads the model using Vue's reactivity and a key binding.

### PromptBar Component
- Provides a text input for model ID and an update button.
- Uses design tokens for spacing, color, and typography.
- Emits update events to parent to trigger viewer reload.

### SpeckleViewer Component
- Receives model URL, authentication token, and server URL as props/environment variables.
- Handles loading, error, and viewer-ready states.
- Uses a key binding to force re-mount on model URL change.

### .env and Config
- `.env` stores Speckle token and server URL for secure access.
- `modelConfig.js` stores project and model IDs for each viewer panel.

### User Flow
1. User sees default model loaded from config.
2. User enters a new model ID in PromptBar and clicks update.
3. Viewer reloads with new model, keeping project ID fixed.

### Design Tokens Used
- Colors: `--navy-blue-100`, `--light-lila-100`, `--fucsia-100`, etc.
- Spacing: `--space-md`, `--space-lg`
- Border radius: `--radius-medium`
- Shadows: `--shadow-md`, `--shadow-lg`
- Typography: Inter font, type scale

### Accessibility & Responsiveness
- PromptBar and ViewerContent are keyboard accessible.
- Layout adapts for mobile and desktop screens.
