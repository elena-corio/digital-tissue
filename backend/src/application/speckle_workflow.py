from specklepy.transports.server import ServerTransport
from adapters.speckle.get_client import get_client
from adapters.speckle.get_latest_version import get_latest_version
from adapters.speckle.receive_data import receive_data
from config import PROJECT_ID

def run_application():
    client = get_client()
    version = get_latest_version(client)
    if version:
        transport = ServerTransport(stream_id=PROJECT_ID, client=client)
        data = receive_data(version, transport)
        print(data)