from specklepy.transports.server import ServerTransport
from adapters.speckle.get_client import get_client
from adapters.speckle.get_latest_version import get_latest_version
from adapters.speckle.receive_data import receive_data
from config import PROJECT_ID
from application.metrics_service import calculate_and_save_metrics

def run_application():
    client = get_client()
    version = get_latest_version(client)
    if not version:
        print("No versions found. Exiting.")
        return
    
    transport = ServerTransport(stream_id=PROJECT_ID, client=client)
    model = receive_data(version, transport)
    
    # Calculate and save all metrics
    metrics = calculate_and_save_metrics(version.id, model)
    
    return metrics