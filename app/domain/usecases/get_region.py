from app.domain.repository.db.region import RegionRepository
from uuid import UUID


async def get_region_usecase(region_id: UUID, region_repo: RegionRepository):
    region_props = await region_repo.get_by_id(region_id)
    return region_props