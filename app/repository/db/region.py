from typing import Any, Type
from uuid import UUID

from app.shared.repository.db.base import BaseDBRepository
from app.domain.repository.db.region import RegionRepository
from app.domain.data.region import RegionProps
from app.repository.db.schema.region import Region

class RegionDBRepository(
    BaseDBRepository[RegionProps, Region], RegionRepository
):
    @property
    def _table(self) -> Type[Region]:
        return Region

    @property
    def _entity(self) -> Type[RegionProps]:
        return RegionProps


    async def filter_by_id(self, id: UUID) -> None:
        async with self._db_session() as session:
            query = self.select().where(self._table.id == id)
            result = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), result.scalars().all())
            )
    
    async def get_all_regions(self):
        async with self._db_session() as session:
            query = (
                self.select()
                .execution_options(synchronize_session="fetch")
            )
            results = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), results.scalars().all())
            )