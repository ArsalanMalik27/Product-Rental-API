from pydantic import Field, BaseModel
from uuid import UUID, uuid4

from app.domain.data.product import ProductProps, CreateProductProps
from app.shared.domain.data.page import PageRequestDTO

from typing import Annotated

class CreateProductDTO(CreateProductProps):
    pass

class ProductResponseDTO(ProductProps):
    pass