from typing import Any, Type
from uuid import UUID

from app.shared.repository.db.base import BaseDBRepository
from app.domain.repository.db.rental_period import RentalPeriodRepository
from app.domain.data.rental_period import RentalPeriodProps
from app.repository.db.schema.rental_period import RentalPeriod

class RentalPeriodDBRepository(
    BaseDBRepository[RentalPeriodProps, RentalPeriod], RentalPeriodRepository
):
    @property
    def _table(self) -> Type[RentalPeriod]:
        return RentalPeriod

    @property
    def _entity(self) -> Type[RentalPeriodProps]:
        return RentalPeriodProps


    async def filter_by_name(self, name: str) -> None:
        async with self._db_session() as session:
            query = self.select().where(self._table.name == name)
            result = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), result.scalars().all())
            )

    async def get_all_rental_periods(self):
        async with self._db_session() as session:
            query = (
                self.select()
                .execution_options(synchronize_session="fetch")
            )
            results = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), results.scalars().all())
            )