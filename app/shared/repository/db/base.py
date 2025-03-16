from abc import abstractmethod
from typing import Any, Generic, Optional, Type, TypeVar
from uuid import UUID

from sqlalchemy import func, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.shared.domain.data.entity import Entity
from app.shared.domain.data.page import PageMetadata
from app.shared.domain.repository.db.base import BaseRepository
from app.shared.repository.db.schema.base import BaseTableMixin
from app.shared.utils.error import DomainError

ENTITY_TYPE = TypeVar("ENTITY_TYPE", bound=Entity)
TABLE_TYPE = TypeVar("TABLE_TYPE", bound=BaseTableMixin)


class BaseDBRepository(Generic[ENTITY_TYPE, TABLE_TYPE], BaseRepository[ENTITY_TYPE]):
    @property
    @abstractmethod
    def _table(self) -> Type[TABLE_TYPE]:
        ...

    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session = db_session

    def select(self) -> Any:
        return select(self._table).where(self._table.deleted == False)

    async def create(self, entity: ENTITY_TYPE) -> None:
        async with self._db_session() as session:
            query = self._table(**entity.dict())
            session.add(query)
            await session.commit()
    
    async def paginate(
        self, query: Any, page: int, page_size: int
    ) -> tuple[list[TABLE_TYPE], PageMetadata]:
        async with self._db_session() as session:
            if page <= 0:
                raise DomainError("page should be be >= 1")
            if page_size <= 0:
                raise DomainError("page_size should be >= 1")
            paginated_query = query.limit(page_size).offset((page - 1) * page_size)
            count_query = query.with_only_columns(func.count(self._table.id))
            results = await session.execute(paginated_query)
            responses = results.scalars().unique().all()
            if len(responses) >= 1:
                total_result = await session.execute(count_query)
                page_data = PageMetadata(
                    page=page,
                    page_size=page_size,
                    total=len(responses),
                )
                return (responses, page_data)
            else:
                page_data = PageMetadata(
                    page=0,
                    page_size=0,
                    total=0,
                )
                return ([], page_data)