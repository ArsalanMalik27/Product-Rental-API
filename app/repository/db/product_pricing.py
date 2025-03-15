from typing import Any, Type
from uuid import UUID

from app.shared.repository.db.base import BaseDBRepository
from app.domain.repository.db.product_pricing import ProductPricingRepository 
from app.domain.data.product_pricing import ProductPricingProps
from app.repository.db.schema.product_pricing import ProductPricing

class ProductPricingDBRepository(
    BaseDBRepository[ProductPricingProps, ProductPricing], ProductPricingRepository
):
    @property
    def _table(self) -> Type[ProductPricing]:
        return ProductPricing

    @property
    def _entity(self) -> Type[ProductPricingProps]:
        return ProductPricingProps


    async def filter_by_id(self, id: UUID) -> None:
        async with self._db_session() as session:
            query = self.select().where(self._table.id == id)
            result = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), result.scalars().all())
            )