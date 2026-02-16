import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

# Get the backend directory (parent of src/)
# When running: python src/main.py from /backend, __file__ will resolve correctly
BACKEND_DIR = Path(__file__).parent.parent.parent.resolve()
METRICS_CACHE_DIR = BACKEND_DIR / "metrics_cache"


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
            metric_dict = metric.__dict__.copy()
            
            # Round total_value to 2 decimals
            if 'total_value' in metric_dict and metric_dict['total_value'] is not None:
                metric_dict['total_value'] = round(metric_dict['total_value'], 2)
            
            # Round value_per_level to 2 decimals
            if 'value_per_level' in metric_dict and isinstance(metric_dict['value_per_level'], dict):
                metric_dict['value_per_level'] = {
                    k: round(v, 2) for k, v in metric_dict['value_per_level'].items()
                }
            
            # Round value_per_cluster to 2 decimals
            if 'value_per_cluster' in metric_dict and isinstance(metric_dict['value_per_cluster'], dict):
                metric_dict['value_per_cluster'] = {
                    k: round(v, 2) for k, v in metric_dict['value_per_cluster'].items()
                }
            
            # Round chart_data values to 2 decimals
            if 'chart_data' in metric_dict and hasattr(metric_dict['chart_data'], '__dict__'):
                chart_data_dict = metric_dict['chart_data'].__dict__.copy()
                if 'values' in chart_data_dict and isinstance(chart_data_dict['values'], dict):
                    chart_data_dict['values'] = {
                        k: round(v, 2) for k, v in chart_data_dict['values'].items()
                    }
                metric_dict['chart_data'] = chart_data_dict
            
            serializable_metrics[key] = metric_dict
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
    try:
        all_files = list(METRICS_CACHE_DIR.iterdir())
        json_files = [f for f in all_files if f.suffix == ".json"]
        
        for file_path in json_files:
            version_id = file_path.stem
            versions[version_id] = str(file_path)
    except Exception as e:
        print(f"Error listing metrics: {e}")
    
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


def get_latest_metrics() -> Optional[Dict[str, Any]]:
    """
    Retrieve the most recently saved metrics.
    
    Returns:
        Dictionary of metrics or None if no metrics found
    """
    ensure_cache_dir()
    
    # List all JSON files
    try:
        all_files = list(METRICS_CACHE_DIR.iterdir())
        json_files = [f for f in all_files if f.suffix == ".json"]
    except Exception as e:
        print(f"Error listing metrics: {e}")
        return None
    
    if not json_files:
        return None
    
    # Get the most recently modified file
    latest_file = max(json_files, key=lambda f: f.stat().st_mtime)
    
    try:
        with open(latest_file, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading metrics: {e}")
        return None
