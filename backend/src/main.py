import sys
from pathlib import Path

from dotenv import load_dotenv

# Add parent directory to path so relative imports work
sys.path.insert(0, str(Path(__file__).parent))

# Load backend/.env for local development
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from adapters.api.metrics import router as metrics_router
from application.metrics_workflow import run_application

app = FastAPI(title="Digital Tissue Backend")


def _get_allowed_origins() -> list[str]:
    """Read allowed CORS origins from env, with safe local defaults."""
    import os

    env_origins = os.getenv("CORS_ALLOWED_ORIGINS", "").strip()
    if env_origins:
        return [origin.strip() for origin in env_origins.split(",") if origin.strip()]

    return [
        "http://localhost:5173",
        "http://localhost:5174",
        "https://elena-corio.github.io",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

# Register API routers
app.include_router(metrics_router)


@app.on_event("startup")
def startup_event():
    """Run on app startup - calculate metrics if cache is empty (local only)"""
    import os
    from infrastructure.metrics_storage import list_all_metrics
    
    # Only attempt calculation in local development, not on Render
    if os.getenv("RENDER") is None:  # Not running on Render
        if not list_all_metrics():
            print("No cached metrics found. Calculating metrics...")
            try:
                run_application()
                print("Metrics calculated successfully on startup")
            except Exception as e:
                print(f"Warning: Failed to calculate metrics on startup: {e}")
        else:
            print("Metrics cache found. Skipping calculation.")
    else:
        # On Render, just load from existing metrics_cache
        if list_all_metrics():
            print("Metrics cache found on Render.")
        else:
            print("WARNING: No metrics cache found on Render. Deploy metrics first.")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

