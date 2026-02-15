from domain.metrics.green_space_index import get_green_space_index_metric
from domain.metrics.daylight_potential import get_daylight_potential_metric
from domain.metrics.program_diversity_index import get_program_diversity_index_metric
from domain.metrics.circulation_efficiency import get_circulation_efficiency_metric
from domain.metrics.occupancy_efficiency import get_occupancy_efficiency_metric
from domain.metrics.net_floor_area_ratio import get_net_floor_area_ratio_metric
from domain.metrics.envelope_efficiency import get_envelope_efficiency_metric
from domain.metrics.carbon_efficiency import get_carbon_efficiency_metric
from infrastructure.metrics_storage import save_metrics


def calculate_all_metrics(model):
    """
    Calculate all metrics from the model.
    
    Args:
        model: Model object containing units, facades, levels, clusters
        
    Returns:
        Dictionary of all calculated metrics
    """
    metrics = {
        "green_space_index": get_green_space_index_metric(
            model.units, 
            model.open_spaces, 
            model.levels, 
            model.clusters
        ),
        "daylight_potential": get_daylight_potential_metric(
            model.facades, 
            model.units, 
            model.levels, 
            model.clusters
        ),
        "program_diversity_index": get_program_diversity_index_metric(),
        "circulation_efficiency": get_circulation_efficiency_metric(),
        "occupancy_efficiency": get_occupancy_efficiency_metric(),
        "net_floor_area_ratio": get_net_floor_area_ratio_metric(),
        "envelope_efficiency": get_envelope_efficiency_metric(),
        "carbon_efficiency": get_carbon_efficiency_metric(),
    }
    
    return metrics


def calculate_and_save_metrics(version_id: str, model):
    """
    Calculate all metrics and save to JSON file.
    
    Args:
        version_id: Unique identifier for the Speckle version
        model: Model object containing units, facades, levels, clusters
        
    Returns:
        Dictionary of all calculated metrics
    """
    print(f"Calculating metrics for version {version_id}...")
    
    metrics = calculate_all_metrics(model)
    
    print("Saving metrics to storage...")
    save_metrics(version_id, metrics)
    
    print("Metrics successfully calculated and saved!")
    
    return metrics
