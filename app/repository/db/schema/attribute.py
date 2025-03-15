from sqlalchemy import Column, Integer, String

from app.shared.repository.db.schema.base import Base, BaseTableMixin
from sqlalchemy.orm import mapped_column


class Attribute(BaseTableMixin, Base):
    name = mapped_column(String(255))