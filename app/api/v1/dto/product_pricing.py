from pydantic import Field, BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from app.domain.data.product_pricing import ProductPricingProps, CreateProductPricingProps
from app.shared.domain.data.page import PageRequestDTO

from typing import Annotated

class CreateProductPricingDTO(CreateProductPricingProps):
    product_id : UUID
    region_id : UUID
    rental_period_id : UUID


class ProductPricingResponseDTO(ProductPricingProps):
    pass