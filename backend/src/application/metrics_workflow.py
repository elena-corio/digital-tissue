from specklepy.transports.server import ServerTransport
from adapters.speckle.get_client import get_client
from adapters.speckle.get_latest_version import get_latest_version
from adapters.speckle.mappers import speckle_to_open_space, speckle_to_unit
from adapters.speckle.receive_data import receive_data
from config import PROJECT_ID
from domain.green_space_index import get_green_space_index_metric

def run_application():
    client = get_client()
    version = get_latest_version(client)
    if not version:
        print("No versions found. Exiting.")
        return
    transport = ServerTransport(stream_id=PROJECT_ID, client=client)
    model = receive_data(version, transport)
    
    green_space_index_metric = get_green_space_index_metric(model.units, model.open_spaces, model.levels, model.clusters)
    print(green_space_index_metric)
    
    return green_space_index_metric