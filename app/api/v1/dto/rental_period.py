from pydantic import Field, BaseModel
from uuid import UUID, uuid4

from app.domain.data.rental_period import RentalPeriodProps, CreateRentalPeriodProps
from app.shared.domain.data.page import PageRequestDTO

from typing import Annotated

class CreateRentalPeriodDTO(CreateRentalPeriodProps):
    pass

class RentalPeriodResponseDTO(RentalPeriodProps):
    pass