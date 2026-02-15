from domain.loader import load_metrics
from domain.model.metric import MetricResult

METRICS = load_metrics()


def get_envelope_efficiency_metric() -> MetricResult:
    """
    Calculate the envelope efficiency metric.
    """
    metric = "envelope_efficiency"
    
    return MetricResult(
        name=METRICS[metric]["name"],
        benchmark=METRICS[metric]["benchmark"],
        total_value=None,
        value_per_level={},
        value_per_cluster={},
        action=METRICS[metric]["action"],
        formula=METRICS[metric]["formula"],
        chart_data=None)
