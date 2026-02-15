import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from adapters.api.metrics import router as metrics_router
from application.metrics_workflow import run_application

app = FastAPI(title="Digital Tissue Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",                # Local development
        "https://elena-corio.github.io"       # Production frontend URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(metrics_router)


@app.on_event("startup")
async def startup_event():
    """Run on app startup - calculate metrics if cache is empty"""
    from infrastructure.metrics_storage import list_all_metrics
    
    # Option C: Calculate metrics only if cache is empty
    if not list_all_metrics():
        print("No cached metrics found. Calculating metrics...")
        run_application()
    else:
        print("Metrics cache found. Skipping calculation.")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

