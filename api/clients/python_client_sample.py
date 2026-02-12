import requests

# Sample usage of the REST API from Python
API_URL = "http://localhost:8000/metrics"

response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()
    print("MetricA:", data.get("metricA"))
    print("MetricB:", data.get("metricB"))
else:
    print("Failed to fetch metrics:", response.status_code)
