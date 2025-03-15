from app.shared.domain.data.entity import Entity

from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, List, Any
from app.domain.data.attribute import CreateAttributeProps

class CreateAttributeValuesProps(BaseModel):
    value: str
    attribute: CreateAttributeProps


    class Config:
        from_attributes = True

class AttributeValuesProps(CreateAttributeValuesProps,Entity):
    product_id: UUID
    attribute_id: UUID

@dataclass
class AttributeValues:
    props: AttributeValuesProps

    @staticmethod
    def create_from_props(props: AttributeValuesProps) -> Entity:
        attribute_props = AttributeValuesProps(**props.dict(),id=uuid4(),created_at=datetime.now(),updated_at=datetime.now())
        return AttributeValues(props=attribute_props)