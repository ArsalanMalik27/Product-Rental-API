from app.shared.domain.data.entity import Entity

from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime


class CreateRegionProps(BaseModel):
    name: str

    class Config:
        from_attributes = True

class RegionProps(CreateRegionProps,Entity):
    pass

@dataclass
class Region:
    props: RegionProps

    @staticmethod
    def create_from_props(props: RegionProps) -> Entity:
        region_props = RegionProps(**props.dict(),id=uuid4(),created_at=datetime.now(),updated_at=datetime.now())
        return Region(props=region_props)