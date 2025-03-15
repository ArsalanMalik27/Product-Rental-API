from typing import Any, Type
from uuid import UUID

from app.shared.repository.db.base import BaseDBRepository
from app.domain.repository.db.attribute import AttributeRepository
from app.domain.data.attribute import AttributeProps
from app.repository.db.schema.attribute import Attribute

class AttributeDBRepository(
    BaseDBRepository[AttributeProps, Attribute], AttributeRepository
):
    @property
    def _table(self) -> Type[Attribute]:
        return Attribute

    @property
    def _entity(self) -> Type[AttributeProps]:
        return AttributeProps


    async def filter_by_name(self, name: str) -> None:
        async with self._db_session() as session:
            query = self.select().where(self._table.name == name)
            result = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), result.scalars().all())
            )

    async def get_all_attributes(self):
        async with self._db_session() as session:
            query = (
                self.select()
                .execution_options(synchronize_session="fetch")
            )
            results = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), results.scalars().all())
            )