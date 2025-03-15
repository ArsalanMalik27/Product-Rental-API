from app.domain.data.region import Region, CreateRegionProps
from app.api.v1.dto.region import CreateRegionDTO
from app.domain.repository.db.region import RegionRepository

async def create_region_usecase(create_region_dto:CreateRegionDTO, region_repo: RegionRepository):
    region_props = CreateRegionProps(**create_region_dto.dict())
    region = Region.create_from_props(region_props)
    await region_repo.create(region.props)
    return region.props