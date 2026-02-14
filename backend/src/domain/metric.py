from dataclasses import dataclass
import string


@dataclass
class TabledataPoint:
    label: string
    item: enumerate
    count: float
    quantity: float
    unit: string
    
@dataclass
class ChartDataPoint:
    label: string
    values: dict[enumerate, float]
    
@dataclass
class MetricResult:
    name: string
    final_value: float
    benchmark: float
    chart: ChartDataPoint
    table: TabledataPoint
    viewer_filter: enumerate
    action: string
