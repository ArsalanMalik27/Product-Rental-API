from app.domain.repository.db.rental_period import RentalPeriodRepository
from uuid import UUID

async def get_rental_period_usecase(rental_period_id : UUID, rental_period_repo: RentalPeriodRepository):
    rental_period_props = await rental_period_repo.get_by_id(rental_period_id)
    return rental_period_props