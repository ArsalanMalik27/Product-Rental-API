from pydantic import Field, BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from app.domain.data.attribute_values import AttributeValuesProps, CreateAttributeValuesProps
from app.shared.domain.data.page import PageRequestDTO

from typing import Annotated

class CreateAttributeValuesDTO(CreateAttributeValuesProps):
    product_id: UUID
    attribute_id: UUID


class AttributeValuesResponseDTO(AttributeValuesProps):
    pass