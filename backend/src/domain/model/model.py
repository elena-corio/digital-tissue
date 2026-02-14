from dataclasses import dataclass
import string

from domain.model.enum import MaterialType, ProgramType, SectionType

@dataclass
class ModelElement:
    cluster_id: string
    speckle_type: string
    geometry: any
    level: int

@dataclass
class Unit (ModelElement):
    name: ProgramType
    area: float

@dataclass
class MeshElement(ModelElement):
    material: MaterialType
    area: float
    thickness: float
    
@dataclass
class CurveElement(ModelElement):
    material: MaterialType
    length: float
    section: SectionType
    size: float
    
@dataclass
class Facade(MeshElement):
    pass
    
@dataclass
class Slabs(MeshElement):
    pass
    
@dataclass
class Core(CurveElement):
    pass

@dataclass
class Column(CurveElement):
    pass
