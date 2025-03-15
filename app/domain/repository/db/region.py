from abc import ABCMeta, abstractmethod
from typing import Optional
from uuid import UUID

from app.domain.data.region import RegionProps
from app.shared.domain.repository.db.base import BaseRepository


class RegionRepository(BaseRepository[RegionProps]):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def filter_by_name(self, name: str) -> None:
        raise NotImplementedError("Subclass should implement this")