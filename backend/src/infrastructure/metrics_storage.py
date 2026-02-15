import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any


METRICS_CACHE_DIR = Path(__file__).parent.parent.parent / "metrics_cache"


def ensure_cache_dir():
    """Create metrics_cache directory if it doesn't exist."""
    METRICS_CACHE_DIR.mkdir(parents=True, exist_ok=True)


def save_metrics(version_id: str, metrics: Dict[str, Any]) -> None:
    """
    Save metrics to a JSON file.
    
    Args:
        version_id: Unique identifier for the Speckle version
        metrics: Dictionary of calculated metrics
    """
    ensure_cache_dir()
    
    file_path = METRICS_CACHE_DIR / f"{version_id}.json"
    
    # Convert MetricResult objects to dicts for JSON serialization
    serializable_metrics = {}
    for key, metric in metrics.items():
        if hasattr(metric, '__dict__'):
            serializable_metrics[key] = metric.__dict__
        else:
            serializable_metrics[key] = metric
    
    with open(file_path, "w") as f:
        json.dump(serializable_metrics, f, indent=2, default=str)
    
    print(f"Metrics saved to {file_path}")


def get_metrics(version_id: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve metrics from a JSON file.
    
    Args:
        version_id: Unique identifier for the Speckle version
        
    Returns:
        Dictionary of metrics or None if not found
    """
    file_path = METRICS_CACHE_DIR / f"{version_id}.json"
    
    if not file_path.exists():
        print(f"No metrics found for version {version_id}")
        return None
    
    with open(file_path, "r") as f:
        return json.load(f)


def list_all_metrics() -> Dict[str, str]:
    """
    List all saved metric versions with their file paths.
    
    Returns:
        Dictionary mapping version_id to file path
    """
    ensure_cache_dir()
    
    versions = {}
    for file_path in METRICS_CACHE_DIR.glob("*.json"):
        version_id = file_path.stem
        versions[version_id] = str(file_path)
    
    return versions


def delete_metrics(version_id: str) -> bool:
    """
    Delete metrics for a specific version.
    
    Args:
        version_id: Unique identifier for the Speckle version
        
    Returns:
        True if deleted, False if not found
    """
    file_path = METRICS_CACHE_DIR / f"{version_id}.json"
    
    if file_path.exists():
        file_path.unlink()
        print(f"Metrics deleted for version {version_id}")
        return True
    
    return False
