from app.shared.domain.data.entity import Entity

from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, List, Any, Dict

from app.domain.data.region import CreateRegionProps
from app.domain.data.rental_period import CreateRentalPeriodProps

class CreateProductPricingProps(BaseModel):
    product_id : UUID
    region_id : UUID
    rental_period_id : UUID
    

    class Config:
        from_attributes = True

class ProductPricingViewProps(BaseModel):
    region : Optional[CreateRegionProps]
    rental_period : Optional[CreateRentalPeriodProps]
    price : float
    currency: str = 'USD'

    class Config:
        from_attributes = True

class ProductPricingProps(CreateProductPricingProps,Entity):
    pass

@dataclass
class ProductPricing:
    props: ProductPricingProps

    @staticmethod
    def create_from_props(props: CreateProductPricingProps) -> Entity:
        product_pricing_props = ProductPricingProps(**props.dict(),id=uuid4(),created_at=datetime.now(),updated_at=datetime.now())
        return ProductPricing(props=product_pricing_props)