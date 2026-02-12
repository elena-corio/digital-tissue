from fastapi import FastAPI
from adapters.api.metrics import router as metrics_router

app = FastAPI(title="Digital Tissue Backend")

# Register API routers
app.include_router(metrics_router)
