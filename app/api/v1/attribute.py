
from app.api.v1.dto.attribute import CreateAttributeDTO, AttributeResponseDTO
from app.container import Container

from app.domain.usecases.create_attribute import create_attribute_usecase
from app.domain.usecases.get_attribute_list import get_attribute_list_usecase

from app.repository.db.attribute import AttributeDBRepository

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Request
from typing import List

router = APIRouter()


@router.post("/add",response_model=AttributeResponseDTO)
@inject
async def add_attribute(
    create_attribute_dto: CreateAttributeDTO,
    attribute_repo: AttributeDBRepository = Depends(Provide[Container.attribute_db_repository]),
    ) -> AttributeResponseDTO:
    response = await create_attribute_usecase(create_attribute_dto,attribute_repo)
    return response

@router.get("/",response_model=List[AttributeResponseDTO])
@inject
async def get_attribute(
    attribute_repo: AttributeDBRepository = Depends(Provide[Container.attribute_db_repository]),
    )->List[AttributeResponseDTO]:
    response = await get_attribute_list_usecase(attribute_repo)
    return response