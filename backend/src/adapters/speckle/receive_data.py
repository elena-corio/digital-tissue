from dataclasses import dataclass
from typing import Any, Dict
from specklepy.api import operations

@dataclass
class Item:
    geometry: Any
    properties: Dict[str, Any]

@dataclass
class Collection:
    name: str
    items: list[Item]
    
def receive_data(version, transport):
    # Receive the full data tree
    obj = operations.receive(version.referenced_object, transport)


    print(f"Project: {obj.name}")
    for element in obj.elements:
        for child in element.elements:
            #print(f"    Child: {child.speckle_type}")
            #print(f"        Properties: {child.properties}")
            if child.speckle_type == "Objects.Geometry.Mesh":
                #print(child.__dict__.keys())
                print(f"        Points: {child.area}")
               
            