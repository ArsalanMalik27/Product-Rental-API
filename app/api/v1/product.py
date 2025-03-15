
from app.api.v1.dto.product import CreateProductDTO, ProductResponseDTO
from app.container import Container

from app.domain.usecases.create_product import create_product_usecase
from app.domain.usecases.get_products_list import get_products_list_usecase

from app.repository.db.product import ProductDBRepository

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Request
from typing import List
router = APIRouter()


@router.post("/add",response_model=ProductResponseDTO)
@inject
async def add_product(
    create_product_dto: CreateProductDTO,
    product_repo: ProductDBRepository = Depends(Provide[Container.product_db_repository]),
    ) -> ProductResponseDTO:
    response = await create_product_usecase(create_product_dto,product_repo)
    return response

@router.get("/",response_model=List[ProductResponseDTO])
@inject
async def get_products(
    product_repo: ProductDBRepository = Depends(Provide[Container.product_db_repository]),
    ) -> List[ProductResponseDTO]:
    response = await get_products_list_usecase(product_repo)
    return response