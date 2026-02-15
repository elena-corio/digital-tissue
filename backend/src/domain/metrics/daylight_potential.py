from domain.loader import load_metrics
from domain.model.enum import MaterialType
from domain.model.metric import MetricResult
from domain.model.elements import Facade, Unit


METRICS = load_metrics()

def calculate_daylight_potential(facades: list[Facade], units: list[Unit]) -> float:
    """
    Calculate the daylight potential of a facade based on its area and the program's area.
    """
    windows = list(filter(lambda facade: facade.material == MaterialType.GLASS, facades))
    windows_area = sum(window.area for window in windows)
    program_area = sum(unit.area for unit in units)
    
    if program_area == 0:
        return 0.0
    
    return windows_area / program_area

def calculate_daylight_potential_per_level(facades: list[Facade], units: list[Unit], levels: list[int]) -> dict[int, float]:
    value_per_level = {}
    for level in levels:
        level_units = list(filter(lambda unit: unit.level == level, units))
        level_facades = list(filter(lambda facade: facade.level == level, facades))
        if not level_units:  # Skip levels with no units
            continue
        value_per_level[level] = calculate_daylight_potential(level_facades, level_units)
    return value_per_level


def calculate_daylight_potential_per_cluster(facades: list[Facade], units: list[Unit], clusters: list[str]) -> dict[str, float]:
    value_per_cluster = {}
    for cluster in clusters:
        cluster_units = list(filter(lambda unit: unit.cluster_id == cluster, units))
        cluster_facades = list(filter(lambda facade: facade.cluster_id == cluster, facades))
        if not cluster_units:  # Skip clusters with no units
            continue
        value_per_cluster[cluster] = calculate_daylight_potential(cluster_facades, cluster_units)
    return value_per_cluster


def get_daylight_potential_metric(facades: list[Facade], units: list[Unit], levels: list[int], clusters: list[str]) -> MetricResult:
    """
    Calculate the overall daylight potential metric for a list of facades and units.
    """
    value_per_level = calculate_daylight_potential_per_level(facades, units, levels)
    value_per_cluster = calculate_daylight_potential_per_cluster(facades, units, clusters)
    total_value = calculate_daylight_potential(facades, units)
    
    
    metric = "daylight_potential"
    
    return MetricResult(
        name=METRICS[metric]["name"],  
        benchmark=METRICS[metric]["benchmark"],
        total_value=total_value,
        value_per_level=value_per_level,
        value_per_cluster=value_per_cluster,
        chart_data=None,
        action=METRICS[metric]["action"],
        formula=METRICS[metric]["formula"]
        ) 