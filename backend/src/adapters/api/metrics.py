from fastapi import APIRouter, HTTPException
from infrastructure.metrics_storage import get_metrics, list_all_metrics

router = APIRouter(prefix="/api/metrics", tags=["metrics"])


@router.get("/{version_id}")
async def fetch_metrics(version_id: str):
    """
    Fetch cached metrics for a specific Speckle version.
    
    Args:
        version_id: Unique identifier for the Speckle version
        
    Returns:
        Dictionary of metrics or error if not found
    """
    metrics = get_metrics(version_id)
    
    if metrics is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Metrics not found for version {version_id}"
        )
    
    return metrics


@router.get("")
async def list_saved_metrics():
    """
    List all saved metric versions.
    
    Returns:
        Dictionary mapping version_id to file path
    """
    versions = list_all_metrics()
    
    if not versions:
        return {"message": "No metrics cached yet", "versions": {}}
    
    return {"message": f"Found {len(versions)} cached versions", "versions": versions}