
from app.api.v1.dto.product_pricing import CreateProductPricingDTO, ProductPricingResponseDTO
from app.api.v1.dependency.product_pricing import valid_product_pricing_dto
from app.container import Container

from app.domain.usecases.create_product_pricing import create_product_pricing_usecase

from app.repository.db.product_pricing import ProductPricingDBRepository

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Request
from typing import List

router = APIRouter()


@router.post("/add",response_model=ProductPricingResponseDTO)
@inject
async def add_attribute(
    create_product_pricing_dto: CreateProductPricingDTO = Depends(valid_product_pricing_dto),
    product_pricing_repo: ProductPricingDBRepository = Depends(Provide[Container.product_pricing_db_repository]),
    ) -> ProductPricingResponseDTO:
    response = await create_product_pricing_usecase(create_product_pricing_dto,product_pricing_repo)
    return response
