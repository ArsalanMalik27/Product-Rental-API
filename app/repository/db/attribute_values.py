from typing import Any, Type
from uuid import UUID

from app.shared.repository.db.base import BaseDBRepository
from app.domain.repository.db.attribute_values import AttributeValuesRepository 
from app.domain.data.attribute_values import AttributeValuesProps
from app.repository.db.schema.attribute_values import AttributeValues

class AttributeValuesDBRepository(
    BaseDBRepository[AttributeValuesProps, AttributeValues], AttributeValuesRepository
):
    @property
    def _table(self) -> Type[AttributeValues]:
        return AttributeValues

    @property
    def _entity(self) -> Type[AttributeValuesProps]:
        return AttributeValuesProps


    async def filter_by_id(self, id: UUID) -> None:
        async with self._db_session() as session:
            query = self.select().where(self._table.id == id)
            result = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), result.scalars().all())
            )