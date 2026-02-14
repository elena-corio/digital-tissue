from domain.loader import load_metrics, load_rulebook
from domain.model.enum import ProgramType
from domain.model.metric import MetricResult
from domain.model.model import Unit

RULEBOOK = load_rulebook()
METRICS = load_metrics()

def is_green_program(program: ProgramType, rulebook: dict) -> bool:
    return rulebook["program_types"][program.value]["is_green"]

def calculate_green_space_index(res_unit: Unit, green_units: list[Unit]) -> float:
    """
    Calculate the green space index based on the level gap to the nearest green space.
    """
    level_gap = 100.0
    for green_unit in green_units:
        new_level_gap = abs(res_unit.level - green_unit.level)
        if new_level_gap < level_gap:
            level_gap = new_level_gap
    
    return level_gap


def calculate_green_space_index_avg(res_units: list[Unit], green_units: list[Unit]) -> float:
    if not res_units:
        return 0.0
    return sum(calculate_green_space_index(res_unit, green_units) for res_unit in res_units) / len(res_units)

def calculate_green_space_index_per_level(res_units: list[Unit], green_units: list[Unit], levels: list[int]) -> dict[int, float]:
    value_per_level = {}
    for level in levels:
        level_res_units = list(filter(lambda unit: unit.level == level, res_units))
        if not level_res_units:
            continue
        value_per_level[level] = calculate_green_space_index_avg(level_res_units, green_units)
    return value_per_level

def calculate_green_space_index_per_cluster(res_units: list[Unit], green_units: list[Unit], clusters: list[str]) -> dict[str, float]:
    value_per_cluster = {}
    for cluster in clusters:
        cluster_res_units = list(filter(lambda unit: unit.cluster_id == cluster, res_units))
        if not cluster_res_units:
            continue
        value_per_cluster[cluster] = calculate_green_space_index_avg(cluster_res_units, green_units)
    return value_per_cluster

def get_green_space_index_metric(units: list[Unit], levels: list[int], clusters: list[str]) -> MetricResult:
    """
    Calculate the overall green space index metric for a list of units.
    """
    residential_units = list(filter(lambda unit: unit.name in [ProgramType.LIVING, ProgramType.COMMUNITY], units))
    green_units = list(filter(lambda unit: is_green_program(unit.name, RULEBOOK), units))
    total_value = calculate_green_space_index_avg(residential_units, green_units)
    value_per_level = calculate_green_space_index_per_level(residential_units, green_units, levels)
    value_per_cluster = calculate_green_space_index_per_cluster(residential_units, green_units, clusters)
    
    name = "Green Space Index"
    
    return MetricResult(
        name=name,  
        benchmark=METRICS[name]["benchmark"],
        total_value=total_value,
        value_per_level=value_per_level,
        value_per_cluster=value_per_cluster,
        chart_data=None,
        viewer_filter="units",
        action=METRICS[name]["action"])
