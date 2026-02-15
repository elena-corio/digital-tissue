from dataclasses import dataclass

@dataclass
class ChartData:
    label: str
    values: dict[str, float]
    
@dataclass
class MetricResult:
    name: str
    benchmark: float
    total_value: float
    value_per_level: dict[int, float]
    value_per_cluster: dict[str, float]
    chart_data: ChartData
    formula: str
    action: str