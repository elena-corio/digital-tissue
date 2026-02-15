from dataclasses import dataclass
from typing import Any, Dict
from specklepy.api import operations

from adapters.speckle.mappers import speckle_to_facade, speckle_to_open_space, speckle_to_unit
from domain.model.model import Model
    
def receive_data(version, transport):
    # Receive the full data tree
    data = operations.receive(version.referenced_object, transport)
    units_collection = next(collection for collection in data.elements if collection.name == "UNITS")
    units = [speckle_to_unit(u) for u in units_collection.elements]
    
    open_spaces_collection = next(collection for collection in data.elements if collection.name == "OPEN_SPACES")
    green_spaces = [speckle_to_open_space(gs) for gs in open_spaces_collection.elements]
    
    facades_collection = next(collection for collection in data.elements if collection.name == "FACADES")
    facades = [speckle_to_facade(f) for f in facades_collection.elements]
    
    levels = set(unit.level for unit in units)
    clusters = set(unit.cluster_id for unit in units)
    
    return Model(units=units, open_spaces=green_spaces, facades=facades, levels=list(levels), clusters=list(clusters))