
import json
from pathlib import Path

def load_metrics():
    metrics_path = Path(__file__).parent / "json" / "metrics.json"
    with open(metrics_path) as f:
        return json.load(f)
    
def load_rulebook():
    rulebook_path = Path(__file__).parent / "json" / "rulebook.json"
    with open(rulebook_path) as f:
        return json.load(f)