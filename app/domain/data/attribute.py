from app.shared.domain.data.entity import Entity

from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime


class CreateAttributeProps(BaseModel):
    name: str

    class Config:
        from_attributes = True

class AttributeProps(CreateAttributeProps,Entity):
    pass

@dataclass
class Attribute:
    props: AttributeProps

    @staticmethod
    def create_from_props(props: AttributeProps) -> Entity:
        attribute_props = AttributeProps(**props.dict(),id=uuid4(),created_at=datetime.now(),updated_at=datetime.now())
        return Attribute(props=attribute_props)