
from app.api.v1.dto.product import ( 
    CreateProductDTO, 
    ProductResponseDTO, 
    GetProductRequestDTO, 
    GetProductResponseDTO, 
    CreateProductResponseDTO
)
from app.container import Container

from app.domain.usecases.create_product import create_product_usecase
from app.domain.usecases.get_products_list import get_products_list_usecase

from app.repository.db.product import ProductDBRepository

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Request
from uuid import UUID
from typing import List, Optional
from app.shared.domain.data.page import PageRequestDTO,Page

router = APIRouter()


@router.post("/add",response_model=CreateProductResponseDTO)
@inject
async def add_product(
    create_product_dto: CreateProductDTO,
    product_repo: ProductDBRepository = Depends(Provide[Container.product_db_repository]),
    ) -> CreateProductResponseDTO:
    response = await create_product_usecase(create_product_dto,product_repo)
    return response

@router.get("/",response_model=Optional[GetProductResponseDTO])
@inject
async def get_products(
    get_products_request_params: GetProductRequestDTO = Depends(GetProductRequestDTO),
    product_repo: ProductDBRepository = Depends(Provide[Container.product_db_repository]),
    ) -> Optional[GetProductResponseDTO]:
    response = await get_products_list_usecase(product_repo, get_products_request_params)
    return response