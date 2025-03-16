from  app.domain.repository.db.rental_period import RentalPeriodRepository
from app.api.v1.dto.rental_period import CreateRentalPeriodDTO
from  app.domain.data.rental_period import CreateRentalPeriodProps, RentalPeriodProps, RentalPeriod
from app.shared.utils.error import DomainError

async def create_rental_period_usecase(
    create_rental_period_dto: CreateRentalPeriodDTO,
    rental_period_repo: RentalPeriodRepository
    ):
    if create_rental_period_dto.duration_months < 1:
        raise DomainError("Duration months should be greater than 1")
    create_rental_period_props = CreateRentalPeriodProps(**create_rental_period_dto.dict())
    rental_period = RentalPeriod.create_from_props(create_rental_period_props)
    await rental_period_repo.create(rental_period.props)
    return  rental_period.props