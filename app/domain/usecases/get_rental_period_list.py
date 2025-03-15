from app.domain.repository.db.rental_period import RentalPeriodRepository

async def get_rental_period_list_usecase(renal_period_repo: RentalPeriodRepository):
    renal_period_props_list = await renal_period_repo.get_all_rental_periods()
    return renal_period_props_list