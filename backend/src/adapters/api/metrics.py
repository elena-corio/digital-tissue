from fastapi import APIRouter, HTTPException, Depends, Header
import os
import logging
logger = logging.getLogger("metrics")

# Dependency for API key protection
def verify_api_key(x_api_key: str = Header(...)):
    expected_key = os.getenv("API_KEY")
    if not expected_key or x_api_key != expected_key:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return True
from specklepy.transports.server import ServerTransport
from adapters.speckle.get_client import get_client
from adapters.speckle.get_latest_version import get_latest_version
from adapters.speckle.receive_data import receive_data
from config import PROJECT_ID
from infrastructure.metrics_storage import get_metrics, get_latest_metrics, list_all_metrics
from application.metrics_service import calculate_and_save_metrics
import json
from pathlib import Path

router = APIRouter(prefix="/api/metrics", tags=["metrics"])


def _load_metric_definitions():
    """Load metric definitions from metrics.json"""
    json_path = Path(__file__).parent.parent.parent / "domain" / "json" / "metrics.json"
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("metrics.json not found at %s", json_path)
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
async def fetch_latest_metrics():
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
async def list_saved_metrics():
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
async def calculate_metrics(_=Depends(verify_api_key)):
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
            logger.error("No versions found in Speckle project for metrics calculation")
            raise HTTPException(
                status_code=404,
                detail="No versions found in Speckle project"
            )
        transport = ServerTransport(stream_id=PROJECT_ID, client=client)
        model = receive_data(version, transport)
        # Calculate and save metrics
        metrics = calculate_and_save_metrics(version.id, model)
        logger.info("Metrics calculated successfully for version %s", version.id)
        return {"message": "Metrics calculated successfully", "metrics": metrics}
    except Exception as e:
        logger.exception("Error calculating metrics: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Error calculating metrics. See server logs for details."
        )


@router.get("/{version_id}")
async def fetch_metrics(version_id: str):
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