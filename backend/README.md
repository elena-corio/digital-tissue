# Local Development


## How to Start the Backend

1. Open a terminal and navigate to the backend folder:
	```sh
	cd backend
	```
2. Install dependencies (if not already done):
	```sh
	uv sync --active
	```
3. Start the backend server by running:
	```sh
	python main.py
	```
4. Run tests
	```sh
	cd backend
	..\.venv\Scripts\pytest
	```

This will launch the backend at http://127.0.0.1:8000 (or http://localhost:8000).

Alternatively, you can still use uvicorn directly if you prefer:
	```sh
	uvicorn main:app --reload
	```

# Backend Structure (Hexagonal Architecture)

- `domain/` – Core business logic, entities, value objects
- `application/` – Use cases, service interfaces
- `infrastructure/` – External services, DB, Speckle, webhooks, etc.
- `adapters/` – API (REST), CLI, other interfaces
- `main.py` – App entrypoint (FastAPI app)
- `requirements.txt` – Python dependencies

This structure supports clean separation of concerns and scalability.
