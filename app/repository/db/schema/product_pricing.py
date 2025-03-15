from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.shared.repository.db.schema.base import Base, BaseTableMixin
from sqlalchemy.orm import mapped_column, relationship

from app.repository.db.schema.region import Region
from app.repository.db.schema.rental_period import RentalPeriod


class ProductPricing(BaseTableMixin, Base):
    price = mapped_column(Float)
    product_id = mapped_column(
        UUID(as_uuid=True), ForeignKey("product.id", ondelete="CASCADE")
    )
    region_id = mapped_column(
        UUID(as_uuid=True), ForeignKey("region.id", ondelete="CASCADE"), nullable=True
    )
    rental_period_id = mapped_column(
        UUID(as_uuid=True), ForeignKey("rentalperiod.id", ondelete="CASCADE"), nullable=True
    )

    #relationships
    region = relationship("Region", foreign_keys=[region_id], lazy="joined")
    rental_period = relationship("RentalPeriod",foreign_keys=[rental_period_id], lazy="joined")

