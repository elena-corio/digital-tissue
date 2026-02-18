import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import get_cors_allowed_origins
from adapters.api.metrics import router as metrics_router
from application.metrics_workflow import run_application

app = FastAPI(title="Digital Tissue Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
        import logging
        logger = logging.getLogger("startup")
        if not list_all_metrics():
            logger.info("No cached metrics found. Calculating metrics...")
            try:
                run_application()
                logger.info("Metrics calculated successfully on startup")
            except Exception as e:
                logger.warning("Failed to calculate metrics on startup: %s", e, exc_info=True)
        else:
            logger.info("Metrics cache found. Skipping calculation.")
    else:
        # On Render, just load from existing metrics_cache
        if list_all_metrics():
            logger.info("Metrics cache found on Render.")
        else:
            logger.warning("No metrics cache found on Render. Deploy metrics first.")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

