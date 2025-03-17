from app.api.v1.dto.product_pricing import CreateProductPricingDTO

from app.domain.data.product import ProductProps

from app.domain.repository.db.product import ProductRepository
from app.domain.repository.db.region import RegionRepository
from app.domain.repository.db.rental_period import RentalPeriodRepository

from app.domain.usecases.get_product import get_product_usecase
from app.domain.usecases.get_region import get_region_usecase
from app.domain.usecases.get_rental_period import get_rental_period_usecase
from app.shared.utils.error import DomainError


from app.container import Container
from uuid import UUID
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Request

@inject
async def valid_product_pricing_dto(
    create_product_pricing_dto: CreateProductPricingDTO,
    product_repo: ProductRepository = Depends(
        Provide[Container.product_db_repository]
    ),
    region_repo: RegionRepository = Depends(
        Provide[Container.region_db_repository]
    ),
    rental_period_repo: RentalPeriodRepository = Depends(
        Provide[Container.rental_period_db_repository]
    )
) -> CreateProductPricingDTO:
    product_props = await get_product_usecase(create_product_pricing_dto.product_id, product_repo)
    if not product_props:
        raise DomainError("Invalid Product Id")
    region_props = await get_region_usecase(create_product_pricing_dto.region_id, region_repo)
    if not region_props:
        raise DomainError("Invalid Region Id")
    rental_period_props = await get_rental_period_usecase(create_product_pricing_dto.rental_period_id, rental_period_repo)
    if not rental_period_props:
        raise DomainError("Invalid Rental Period Id")
    return create_product_pricing_dto