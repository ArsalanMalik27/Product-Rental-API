from sqlalchemy import Column, Integer, String

from app.shared.repository.db.schema.base import Base, BaseTableMixin
from sqlalchemy.orm import mapped_column, relationship
from app.repository.db.schema.attribute_values import AttributeValues
from app.repository.db.schema.product_pricing import ProductPricing

class Product(BaseTableMixin, Base):
    name = mapped_column(String(255))
    sku = mapped_column(String(255))
    description = mapped_column(String(255))

    attribute_values = relationship("AttributeValues", backref="product", lazy='noload', primaryjoin="and_(AttributeValues.product_id==Product.id, AttributeValues.deleted != True)")
    product_pricing = relationship("ProductPricing", backref="product", lazy='noload', primaryjoin="and_(ProductPricing.product_id==Product.id, ProductPricing.deleted != True)")
