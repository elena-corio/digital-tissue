from fastapi import APIRouter, HTTPException, Depends, Response
from specklepy.transports.server import ServerTransport
from adapters.speckle.get_client import get_client
from adapters.speckle.get_latest_version import get_latest_version
from adapters.speckle.receive_data import receive_data
from config import PROJECT_ID
from infrastructure.metrics_storage import get_metrics, get_latest_metrics, list_all_metrics
from infrastructure.clerk_auth import verify_clerk_token
from application.metrics_service import calculate_and_save_metrics
import json
from pathlib import Path

router = APIRouter(
    prefix="/api/metrics",
    tags=["metrics"]
)


@router.options("", include_in_schema=False)
@router.options("/{path:path}", include_in_schema=False)
async def preflight_handler(path: str = None):
    """Handle CORS preflight requests"""
    return Response(status_code=200)


def _load_metric_definitions():
    """Load metric definitions from metrics.json"""
    json_path = Path(__file__).parent.parent.parent / "domain" / "json" / "metrics.json"
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def _enrich_metrics(calculated_metrics):
    """
    Combine metric definitions with calculated values.
    Adds formula, action, label from metrics.json to calculated values.
    
    Args:
        calculated_metrics: Metrics from cache file
        
    Returns:
        Enriched metrics with definitions merged in
    """
    definitions = _load_metric_definitions()
    enriched = {}
    
    for metric_key, calc_data in calculated_metrics.items():
        if metric_key in definitions:
            definition = definitions[metric_key]
            enriched[metric_key] = {
                # From metrics.json definitions
                "name": definition.get("name"),
                "formula": definition.get("formula"),
                "action": definition.get("action"),
                "label": definition.get("label"),
                # Merge in calculated values
                **calc_data
            }
        else:
            # Keep metrics even if no definition found
            enriched[metric_key] = calc_data
    
    return enriched


@router.get("")
async def fetch_latest_metrics(token: dict = Depends(verify_clerk_token)):
    """
    Fetch the latest calculated metrics enriched with definitions.
    Returns calculated values + names, formulas, benchmarks from backend.
    
    Returns:
        Dictionary of latest metrics with both definitions and values
    """
    metrics = get_latest_metrics()
    
    if metrics is None:
        raise HTTPException(
            status_code=404, 
            detail="No metrics found in cache. Run metrics calculation first."
        )
    
    return _enrich_metrics(metrics)


@router.get("/history")
async def list_saved_metrics(token: dict = Depends(verify_clerk_token)):
    """
    List all saved metric versions (history).
    
    Returns:
        Dictionary mapping version_id to file path
    """
    versions = list_all_metrics()
    
    if not versions:
        return {"message": "No metrics cached yet", "versions": {}}
    
    return {"message": f"Found {len(versions)} cached versions", "versions": versions}


@router.post("/calculate")
async def calculate_metrics(token: dict = Depends(verify_clerk_token)):
    """
    Calculate metrics for the latest Speckle version.
    Triggered by deployment/webhook.
    
    Returns:
        Dictionary of newly calculated metrics
    """
    try:
        # Get latest version and model data
        client = get_client()
        version = get_latest_version(client)
        
        if not version:
            raise HTTPException(
                status_code=404,
                detail="No versions found in Speckle project"
            )
        
        transport = ServerTransport(stream_id=PROJECT_ID, client=client)
        model = receive_data(version, transport)
        
        # Calculate and save metrics
        metrics = calculate_and_save_metrics(version.id, model)
        
        return {"message": "Metrics calculated successfully", "metrics": metrics}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calculating metrics: {str(e)}"
        )


@router.get("/{version_id}")
async def fetch_metrics(version_id: str, token: dict = Depends(verify_clerk_token)):
    """
    Fetch cached metrics for a specific Speckle version, enriched with definitions.
    
    Args:
        version_id: Unique identifier for the Speckle version
        
    Returns:
        Dictionary of metrics with definitions merged in, or error if not found
    """
    metrics = get_metrics(version_id)
    
    if metrics is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Metrics not found for version {version_id}"
        )
    
    return _enrich_metrics(metrics)