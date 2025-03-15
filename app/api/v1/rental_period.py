
from app.api.v1.dto.rental_period import CreateRentalPeriodDTO, RentalPeriodResponseDTO
from app.container import Container

from app.domain.usecases.create_rental_period import create_rental_period_usecase
from app.domain.usecases.get_rental_period_list import get_rental_period_list_usecase

from app.repository.db.rental_period import RentalPeriodDBRepository

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Request
from typing import List

router = APIRouter()


@router.post("/add",response_model=RentalPeriodResponseDTO)
@inject
async def add_rental_period(
    create_rental_period_dto: CreateRentalPeriodDTO,
    rental_period_repo: RentalPeriodDBRepository = Depends(Provide[Container.rental_period_db_repository]),
    ) -> RentalPeriodResponseDTO:
    response = await create_rental_period_usecase(create_rental_period_dto,rental_period_repo)
    return response

@router.get("/")
@inject
async def get_rental_period(
    rental_period_repo: RentalPeriodDBRepository = Depends(Provide[Container.rental_period_db_repository]),
    )->List[RentalPeriodResponseDTO]:
    response = await get_rental_period_list_usecase(rental_period_repo)
    return response