from abc import ABCMeta, abstractmethod
from typing import Optional
from uuid import UUID

from app.domain.data.attribute_values import AttributeValuesProps
from app.shared.domain.repository.db.base import BaseRepository


class AttributeValuesRepository(BaseRepository[AttributeValuesProps]):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def filter_by_id(self, id: UUID) -> None:
        raise NotImplementedError("Subclass should implement this")