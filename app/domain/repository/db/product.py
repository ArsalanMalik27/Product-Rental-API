from abc import ABCMeta, abstractmethod
from typing import Optional
from uuid import UUID

from app.domain.data.product import ProductProps
from app.shared.domain.repository.db.base import BaseRepository


class ProductRepository(BaseRepository[ProductProps]):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def filter_by_id(self, id: UUID) -> None:
        raise NotImplementedError("Subclass should implement this")