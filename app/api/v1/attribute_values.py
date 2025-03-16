
from app.api.v1.dto.attribute_values import CreateAttributeValuesDTO, AttributeValuesResponseDTO
from app.container import Container

from app.domain.usecases.create_attribute_values import create_attribute_values_usecase
from app.domain.usecases.get_attribute_list import get_attribute_list_usecase

from app.repository.db.attribute_values import AttributeValuesDBRepository

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Request
from typing import List

router = APIRouter()


@router.post("/add",response_model=AttributeValuesResponseDTO)
@inject
async def add_attribute(
    create_attribute_values_dto: CreateAttributeValuesDTO,
    attribute_values_repo: AttributeValuesDBRepository = Depends(Provide[Container.attribute_values_db_repository]),
    ) -> AttributeValuesResponseDTO:
    response = await create_attribute_values_usecase(create_attribute_values_dto,attribute_values_repo)
    return response
