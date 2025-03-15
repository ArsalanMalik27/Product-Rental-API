from pydantic import Field, BaseModel
from uuid import UUID, uuid4

from app.domain.data.attribute import AttributeProps, CreateAttributeProps
from app.shared.domain.data.page import PageRequestDTO

from typing import Annotated

class CreateAttributeDTO(CreateAttributeProps):
    pass

class AttributeResponseDTO(AttributeProps):
    pass