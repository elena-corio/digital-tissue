# Digital Tissue Frontend

Vue 3 + Vite frontend application with clean architecture and externalized UI text.

## Project Structure

```
/src
  /config         - Configuration (UI text, constants)
  /components     - Reusable Vue components
    /ui           - Generic UI components
    /buttons      - Button components
    /cards        - Card components
    /layout       - Layout components (Header, Footer)
    /navigation   - Navigation components (NavBar, TabNav)
  /views          - Page components
  /router         - Vue Router configuration
  /assets         - Static assets and styles
```

## Getting Started

Install dependencies:
```bash
npm install
```

Run development server:
```bash
npm run dev
```

Build for production:
```bash
npm run build
```

Preview production build:
```bash
npm run preview
```

## Design Principles

- **No hard-coded UI text**: All strings come from `/src/config/uiText.js`
- **Composable components**: Reusable, single-responsibility components
- **Clean navigation**: Global header with consistent navigation
- **GitHub Pages ready**: Configured with base path for deployment

## Deployment

This project is configured for GitHub Pages deployment. The build output will include the correct base path.

To deploy:
1. Run `npm run build`
2. Deploy the `dist` folder to GitHub Pages
