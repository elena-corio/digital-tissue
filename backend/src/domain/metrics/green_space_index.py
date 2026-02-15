from domain.loader import load_metrics, load_rulebook
from domain.model.enum import ProgramType
from domain.model.metric import ChartData, MetricResult
from domain.model.elements import OpenSpace, Unit

RULEBOOK = load_rulebook()
METRICS = load_metrics()

def is_green_program(program: ProgramType, rulebook: dict) -> bool:
    return rulebook["program_types"][program.value]["is_green"]


def get_level_gap_to_nearest_green(res_unit: Unit, green_spaces: list[OpenSpace]) -> float:
    """
    Calculate the level gap to the nearest green space.
    """
    if not green_spaces:
        return 100.0
    
    return min(abs(res_unit.level - green_space.level) for green_space in green_spaces)


def get_distance_range_entry(level_gap: float, rulebook: dict) -> dict:
    """
    Find the distance range entry for the level gap using max_gap.
    Returns the rulebook entry dict or None if not found.
    """
    for entry in rulebook["green_index_score"]:
        if level_gap <= entry["max_gap"]:
            return entry
    return None


def calculate_green_space_index(res_unit: Unit, green_spaces: list[OpenSpace], rulebook: dict) -> tuple[float, str]:
    """
    Calculate green space index score and distance range for a single unit.
    Returns (score, range_key).
    """
    level_gap = get_level_gap_to_nearest_green(res_unit, green_spaces)
    entry = get_distance_range_entry(level_gap, rulebook)
    
    if entry:
        range_key = f"<{entry['max_gap']}"
        return (entry["score"], range_key)
    
    return (0.0, "unknown")


def calculate_green_space_index_avg(res_units: list[Unit], green_spaces: list[OpenSpace], rulebook: dict) -> tuple[float, dict[str, int]]:
    """
    Calculate average green space index and count units per distance range in single pass.
    Returns (average_score, count_per_range).
    """
    if not res_units:
        return (0.0, {})
    
    total_score = 0.0
    range_counts = {}
    
    # Initialize all ranges to 0
    for entry in rulebook["green_index_score"]:
        range_key = f"<{entry['max_gap']}"
        range_counts[range_key] = 0
    
    # Single pass: calculate score and count
    for res_unit in res_units:
        score, range_key = calculate_green_space_index(res_unit, green_spaces, rulebook)
        total_score += score
        if range_key in range_counts:
            range_counts[range_key] += 1
    
    avg_score = total_score / len(res_units)
    return (avg_score, range_counts)


def calculate_green_space_index_per_level(res_units: list[Unit], green_spaces: list[OpenSpace], levels: list[int], rulebook: dict) -> dict[int, float]:
    """
    Calculate average green space index per level.
    """
    value_per_level = {}
    for level in levels:
        level_res_units = [unit for unit in res_units if unit.level == level]
        if not level_res_units:
            continue
        avg_score, _ = calculate_green_space_index_avg(level_res_units, green_spaces, rulebook)
        value_per_level[level] = avg_score
    return value_per_level


def calculate_green_space_index_per_cluster(res_units: list[Unit], green_spaces: list[OpenSpace], clusters: list[str], rulebook: dict) -> dict[str, float]:
    """
    Calculate average green space index per cluster.
    """
    value_per_cluster = {}
    for cluster in clusters:
        cluster_res_units = [unit for unit in res_units if unit.cluster_id == cluster]
        if not cluster_res_units:
            continue
        avg_score, _ = calculate_green_space_index_avg(cluster_res_units, green_spaces, rulebook)
        value_per_cluster[cluster] = avg_score
    return value_per_cluster


def calculate_distance_range_percentages(range_counts: dict[str, int]) -> dict[str, float]:
    """
    Convert distance range counts to percentages.
    """
    total = sum(range_counts.values())
    if total == 0:
        return {key: 0.0 for key in range_counts}
    
    return {key: round((value / total) * 100, 2) for key, value in range_counts.items()}


def get_green_space_index_metric(units: list[Unit], green_spaces: list[OpenSpace], levels: list[int], clusters: list[str]) -> MetricResult:
    """
    Calculate the overall green space index metric for a list of units.
    """
    residential_units = [unit for unit in units if unit.name in [ProgramType.LIVING, ProgramType.COMMUNITY]]
    
    total_value, distance_range_counts = calculate_green_space_index_avg(residential_units, green_spaces, RULEBOOK)
    value_per_level = calculate_green_space_index_per_level(residential_units, green_spaces, levels, RULEBOOK)
    value_per_cluster = calculate_green_space_index_per_cluster(residential_units, green_spaces, clusters, RULEBOOK)
    distance_range_percentages = calculate_distance_range_percentages(distance_range_counts)
    
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
