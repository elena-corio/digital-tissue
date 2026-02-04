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

## Design Principles

1. **Use design tokens** - Always reference CSS variables, never hard-code values
2. **Single responsibility** - Components do one thing well
3. **Composition over complexity** - Combine simple components
4. **No hard-coded text** - All strings from `uiText.js`
5. **Mobile-first** - Responsive by default

## Component Library (In Progress)

| Component | Purpose | Status |
|-----------|---------|--------|
| Header | Global header with branding | Planned |
| NavBar | Primary navigation | Planned |
| TabNav | Tab navigation | Planned |
| Button | Action trigger | Planned |
| Card | Content container | Planned |
