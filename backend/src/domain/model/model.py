from dataclasses import dataclass
from typing import Any

from domain.model.elements import Column, Core, Facade, OpenSpace, Slabs, Unit

@dataclass
class Model:
    facades: list[Facade]
    #slabs: list[Slabs]
    #cores: list[Core]
    #columns: list[Column]
    units: list[Unit]
    open_spaces: list[OpenSpace]
    levels: list[int]
    clusters: list[str]