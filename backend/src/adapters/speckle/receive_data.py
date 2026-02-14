from specklepy.api import operations

def receive_data(version, transport):
    # Receive the full data tree
    received_data = operations.receive(version.referenced_object, transport)

    return received_data