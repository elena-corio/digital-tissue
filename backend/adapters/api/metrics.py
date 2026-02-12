from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics", tags=["metrics"])
def get_metrics():
    # Dummy data for now; replace with real logic later
    return {"metricA": 42.0, "metricB": 3.14}
