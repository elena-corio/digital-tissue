from domain.loader import load_metrics, load_rulebook
from domain.model.enum import ProgramType
from domain.model.metric import ChartData, MetricResult
from domain.model.elements import OpenSpace, Unit

RULEBOOK = load_rulebook()
METRICS = load_metrics()

def get_distance_to_nearest_green(res_unit: Unit, green_spaces: list[OpenSpace]) -> float:
    """
    Calculate the vertical distance to the nearest green space.
    """
    if not green_spaces:
        return 300.0
    
    return min(abs(res_unit.level - green_space.level) for green_space in green_spaces)


def calculate_green_space_index(res_unit: Unit, green_spaces: list[OpenSpace]) -> float:
    """
    Calculate green space index score for a single unit.
    """
    distance_to_green = get_distance_to_nearest_green(res_unit, green_spaces)
    return max(0, 1 - distance_to_green / 300)


def calculate_green_space_index_avg(res_units: list[Unit], green_spaces: list[OpenSpace]) -> float:
    """
    Calculate green space index score for a single unit.
    """
    return sum(calculate_green_space_index(unit, green_spaces) for unit in res_units) / len(res_units)


def calculate_green_space_index_per_level(res_units: list[Unit], green_spaces: list[OpenSpace], levels: list[int]) -> dict[int, float]:
    """
    Calculate average green space index per level.
    """
    value_per_level = {}
    for level in levels:
        level_res_units = [unit for unit in res_units if unit.level == level]
        if not level_res_units:
            continue
        avg_score = calculate_green_space_index_avg(level_res_units, green_spaces)
        value_per_level[level] = avg_score
    return value_per_level


def calculate_green_space_index_per_cluster(res_units: list[Unit], green_spaces: list[OpenSpace], clusters: list[str]) -> dict[str, float]:
    """
    Calculate average green space index per cluster.
    """
    value_per_cluster = {}
    for cluster in clusters:
        cluster_res_units = [unit for unit in res_units if unit.cluster_id == cluster]
        if not cluster_res_units:
            continue
        avg_score = calculate_green_space_index_avg(cluster_res_units, green_spaces)
        value_per_cluster[cluster] = avg_score
    return value_per_cluster


def calculate_distance_range_percentages(value_per_level: dict[int, float], ranges_count: int = 6) -> dict[str, float]:
    """
    Convert distance range counts to percentages.
    """
    if not value_per_level:
        return {}
    
    values = list(value_per_level.values())
    min_val, max_val = min(values), max(values)
    
    if min_val == max_val:
        return {f"< {max_val:.2f}": 100.0}
    
    range_size = (max_val - min_val) / ranges_count
    boundaries = [min_val + (i + 1) * range_size for i in range(ranges_count)]
    range_counts = [0] * ranges_count
    
    for value in values:
        for i, boundary in enumerate(boundaries):
            if value <= boundary:
                range_counts[i] += 1
                break
    
    total = len(values)
    return {
        f"< {boundaries[i]:.2f}": (count / total) * 100
        for i, count in enumerate(range_counts)
    }


def get_green_space_index_metric(units: list[Unit], green_spaces: list[OpenSpace], levels: list[int], clusters: list[str]) -> MetricResult:
    """
    Calculate the overall green space index metric for a list of units.
    """
    residential_units = [unit for unit in units if unit.name in [ProgramType.LIVING]]
    
    total_value = calculate_green_space_index_avg(residential_units, green_spaces)
    value_per_level = calculate_green_space_index_per_level(residential_units, green_spaces, levels)
    value_per_cluster = calculate_green_space_index_per_cluster(residential_units, green_spaces, clusters)
    distance_range_percentages = calculate_distance_range_percentages(value_per_level)
    
    metric = "green_space_index"
    
    return MetricResult(
        name=METRICS[metric]["name"],  
        benchmark=METRICS[metric]["benchmark"],
        total_value=total_value,
        value_per_level=value_per_level,
        value_per_cluster=value_per_cluster,
        chart_data=ChartData(label=METRICS[metric]["label"], values=distance_range_percentages),
        action=METRICS[metric]["action"],
        formula=METRICS[metric]["formula"]
        )
