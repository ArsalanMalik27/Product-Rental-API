from app.shared.domain.data.entity import Entity
from typing import List, Any, Optional
from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from app.domain.data.attribute_values import AttributeValuesProps, CreateAttributeValuesViewProps
from app.domain.data.product_pricing import ProductPricingProps, ProductPricingViewProps


class CreateProductProps(BaseModel):
    name: str
    description: str
    sku: str

    class Config:
        from_attributes = True


class ProductProps(CreateProductProps,Entity):
    attribute_values: Optional[List[CreateAttributeValuesViewProps]] | None
    product_pricing: Optional[List[ProductPricingViewProps]] | None


@dataclass
class Product:
    props: ProductProps

    @staticmethod
    def create_from(props: CreateProductProps) -> Entity:
        product_props = ProductProps(
            **props.dict(),
            attribute_values = None,
            product_pricing = None,
            id=uuid4(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return Product(props=product_props)