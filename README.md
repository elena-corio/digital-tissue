# Digital Tissue

A living data system for design intelligence. This monorepo contains both the frontend (Vue 3 + Vite) and backend (Python FastAPI) applications, along with documentation and shared API contracts.

## Monorepo Structure

```
digital-tissue/
├── frontend/    # Vue 3 + Vite application (see frontend/README.md)
├── backend/     # Python FastAPI backend (see backend/README.md)
├── api/         # API contracts and client samples
└── docs/        # Project documentation
```

## Getting Started

See the individual README files in the frontend and backend folders for setup and development instructions:

- [frontend/README.md](frontend/README.md)
- [backend/README.md](backend/README.md)

## Data flow

The backend (FastAPI) exposes the /metrics API endpoint, which returns mock metric results (Python).
The frontend (Vue.js) fetches data from /metrics and displays the results.

## Documentation

For detailed documentation, see the [docs/](docs/) folder.

## Contributing

Please see the individual frontend and backend README files for contribution guidelines and development workflow.
