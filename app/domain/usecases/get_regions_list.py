from app.domain.repository.db.region import RegionRepository

async def get_regions_list_usecase(region_repo: RegionRepository):
    regions_props_list = await region_repo.get_all_regions()
    return regions_props_list