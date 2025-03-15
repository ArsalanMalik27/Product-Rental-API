from app.shared.domain.data.entity import Entity

from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime


class CreateRentalPeriodProps(BaseModel):
    duration_months: int

    class Config:
        from_attributes = True

class RentalPeriodProps(CreateRentalPeriodProps,Entity):
    pass

@dataclass
class RentalPeriod:
    props: RentalPeriodProps

    @staticmethod
    def create_from_props(props: CreateRentalPeriodProps) -> Entity:
        rental_period_props = RentalPeriodProps(**props.dict(),id=uuid4(),created_at=datetime.now(),updated_at=datetime.now())
        return RentalPeriod(props=rental_period_props)