# Backend Structure (Hexagonal Architecture)

- `domain/` – Core business logic, entities, value objects
- `application/` – Use cases, service interfaces
- `infrastructure/` – External services, DB, Speckle, webhooks, etc.
- `adapters/` – API (REST), CLI, other interfaces
- `main.py` – App entrypoint (FastAPI app)
- `requirements.txt` – Python dependencies

This structure supports clean separation of concerns and scalability.
