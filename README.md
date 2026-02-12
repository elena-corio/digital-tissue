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

## Backend Setup (FastAPI)

Step-by-step plan:

1. Create a backend folder with a hexagonal architecture structure.
2. Set up a Python virtual environment and install FastAPI and Uvicorn.
3. Create a basic FastAPI app with a /metrics endpoint.
4. (Optional) Connect the backend to your OpenAPI contract in api/openapi.yaml.
5. Show how to run the backend locally.
6. (Optional) Add integration with Specklepy and webhooks.

## Documentation

For detailed documentation, see the [docs/](docs/) folder.

## Contributing

Please see the individual frontend and backend README files for contribution guidelines and development workflow.
