from typing import Any, Type
from uuid import UUID

from app.shared.repository.db.base import BaseDBRepository
from app.domain.repository.db.product import ProductRepository
from app.domain.data.product import ProductProps
from app.repository.db.schema.product import Product
from app.repository.db.schema.attribute import Attribute
from app.repository.db.schema.attribute_values import AttributeValues
from app.repository.db.schema.product_pricing import ProductPricing
from app.repository.db.schema.region import Region
from app.repository.db.schema.rental_period import RentalPeriod
from sqlalchemy.orm import joinedload, contains_eager
from app.shared.domain.data.page import Page, PageMetadata
from sqlalchemy import func, select

from sqlalchemy.orm import aliased
class ProductDBRepository(
    BaseDBRepository[ProductProps, Product], ProductRepository
):
    @property
    def _table(self) -> Type[Product]:
        return Product

    @property
    def _entity(self) -> Type[ProductProps]:
        return ProductProps


    async def filter_by_id(self, id: UUID) -> None:
        async with self._db_session() as session:
            query = self.select().where(self._table.id == id)
            result = await session.execute(query)
            return list(
                map(lambda obj: self._entity.from_orm(obj), result.scalars().all())
            )
    
    async def create_product(self,props : ProductProps):
        async with self._db_session() as session:
            enitity_dict = props.dict(exclude=['attribute_values', 'product_pricing'])
            que = self._table(**enitity_dict)
            session.add(que)
            await session.commit()
    
    async def get_all_products(self, region_id, rental_period_id, page, page_size):
        async with self._db_session() as session:
            query = (
                self.select()
                .outerjoin(
                    AttributeValues, Product.id == AttributeValues.product_id
                )
                .outerjoin(
                    ProductPricing, Product.id == ProductPricing.product_id
                )
                .options(contains_eager(Product.attribute_values))
                .options(contains_eager(Product.product_pricing))
                .group_by(Product, AttributeValues, ProductPricing)
                .execution_options(synchronize_session="fetch")
            )
            if region_id:
                query = query.filter(ProductPricing.region_id == region_id)
            if rental_period_id:
                query = query.filter(ProductPricing.rental_period_id == rental_period_id)
            results, page_metadata = await self.paginate(query, page, page_size)
            items = list(map(lambda obj: self._entity.from_orm(obj), results))
            return Page(items=items, **page_metadata.dict())