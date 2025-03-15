from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.shared.repository.db.schema.base import Base, BaseTableMixin
from sqlalchemy.orm import mapped_column, relationship

from app.repository.db.schema.attribute import Attribute

class AttributeValues(BaseTableMixin, Base):
    value = mapped_column(String(255))

    product_id = mapped_column(
        UUID(as_uuid=True), ForeignKey("product.id", ondelete="CASCADE")
    )
    attribute_id = mapped_column(
        UUID(as_uuid=True), ForeignKey("attribute.id", ondelete="CASCADE"), nullable=True
    )
    
    # relations
    attribute = relationship("Attribute", foreign_keys=[attribute_id], lazy="joined")