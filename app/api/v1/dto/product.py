from pydantic import Field, BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from fastapi import Query
from app.domain.data.product import ProductProps, CreateProductProps
from app.shared.domain.data.page import PageRequestDTO, Page

from typing import Annotated, List, Optional

class CreateProductDTO(CreateProductProps):
    pass

class CreateProductResponseDTO(CreateProductProps):
    id: UUID
    created_at: datetime
    updated_at: datetime
    deleted: bool

class GetProductRequestDTO(PageRequestDTO):
    region_id : Optional[UUID] = Query(default=None, title="region_id")
    rental_period_id : Optional[UUID] = Query(default=None, title="rental_period_id")

class GetProductResponseDTO(Page):
    items: List[ProductProps]

class ProductResponseDTO(ProductProps):
    pass
    