
from app.api.v1.dto.region import CreateRegionDTO, RegionResponseDTO
from app.container import Container

from app.domain.usecases.create_region import create_region_usecase
from app.domain.usecases.get_regions_list import get_regions_list_usecase

from app.repository.db.region import RegionDBRepository

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Request
from typing import List

router = APIRouter()


@router.post("/add",response_model=RegionResponseDTO)
@inject
async def add_region(
    create_region_dto: CreateRegionDTO,
    region_repo: RegionDBRepository = Depends(Provide[Container.region_db_repository]),
    ) -> RegionResponseDTO:
    response = await create_region_usecase(create_region_dto,region_repo)
    return response

@router.get("/",response_model=List[RegionResponseDTO])
@inject
async def get_regions(
    region_repo: RegionDBRepository = Depends(Provide[Container.region_db_repository]),
    )->List[RegionResponseDTO]:
    response = await get_regions_list_usecase(region_repo)
    return response