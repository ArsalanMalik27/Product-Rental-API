from sqlalchemy import Column, Integer, String

from app.shared.repository.db.schema.base import Base, BaseTableMixin
from sqlalchemy.orm import mapped_column


class RentalPeriod(BaseTableMixin, Base):
    duration_months = mapped_column(Integer)