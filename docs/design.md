# Design System

## Color Palette

### Primary & Accent Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--navy-blue-100` | #303179 | Primary brand, headers |
| `--navy-blue-50` | #7d81ac | Hover states, borders |
| `--blue-100` | #3b479f | Interactive elements |
| `--light-blue-100` | #4697e3 | Links, info |
| `--fucsia-100` | #e9268c | CTAs, important actions |
| `--orange-100` | #e7882f | Warnings |
| `--yellow-100` | #f0b43a | Status indicators |

### Neutral Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--light-lila-100` | #d8d9ed | Borders, dividers |
| `--light-lila-50` | #f0f2f9 | Backgrounds |
| `--light-grey-100` | #dadad9 | Secondary borders |
| `--light-grey-50` | #ececec | Subtle backgrounds |

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
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
--space-3xl: 4rem;     /* 64px */
```

## Border Radius

```css
--radius-small: 4px;   /* Buttons, inputs */
--radius-medium: 8px;  /* Cards */
--radius-large: 12px;  /* Modals, panels */
```

## Component Patterns

### Buttons

```css
/* Primary */
.btn-primary {
  background: var(--fucsia-100);
  color: white;
  padding: var(--space-md) var(--space-lg);
  border-radius: var(--radius-small);
}

/* Secondary */
.btn-secondary {
  background: transparent;
  border: 1px solid var(--navy-blue-100);
  color: var(--navy-blue-100);
}
```

### Cards

```css
.card {
  background: white;
  border: 1px solid var(--light-lila-100);
  border-radius: var(--radius-medium);
  padding: var(--space-lg);
}

.card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

### Navigation

```css
/* Active state */
.nav-link-active {
  background: var(--navy-blue-100);
  color: white;
}

/* Tab active */
.tab-button-active {
  border-bottom: 2px solid var(--navy-blue-100);
  color: var(--navy-blue-100);
}
```

## Transitions

```css
--transition-fast: 0.15s ease;  /* Hover states */
--transition-base: 0.2s ease;   /* Buttons, links */
--transition-slow: 0.3s ease;   /* Modals */
```

## Accessibility

- **Contrast**: Minimum 4.5:1 for body text, 3:1 for large text
- **Focus states**: 2px outline with offset
- **Touch targets**: Minimum 44×44px
- **Keyboard navigation**: All interactive elements accessible via Tab

```css
:focus-visible {
  outline: 2px solid var(--navy-blue-100);
  outline-offset: 2px;
}
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
