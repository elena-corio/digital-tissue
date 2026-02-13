from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from adapters.api.metrics import router as metrics_router

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)