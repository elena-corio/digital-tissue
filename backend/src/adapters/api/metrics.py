from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics", tags=["metrics"])
def get_metric_values():
    return {
        "Service Density Index": 0.04,
        "Urban Green Space Index": 0.80,
        "Program Diversity Index": 0.75,
        "Circulation Efficiency Index": 0.65,
        "Circulation Efficiency Index": 0.65,
        "Mixed-Use Area Ratio": 0.65,
        "Column-free Area Ratio": 0.70,
        "Daylight Potential": 0.20,
        "Carbon Efficiency Index": 1.00,
    }