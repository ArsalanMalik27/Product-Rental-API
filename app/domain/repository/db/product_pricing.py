from abc import ABCMeta, abstractmethod
from typing import Optional
from uuid import UUID

from app.domain.data.product_pricing import ProductPricingProps
from app.shared.domain.repository.db.base import BaseRepository


class ProductPricingRepository(BaseRepository[ProductPricingProps]):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def filter_by_id(self, id: UUID) -> None:
        raise NotImplementedError("Subclass should implement this")