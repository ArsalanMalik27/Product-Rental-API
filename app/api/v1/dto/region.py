from pydantic import Field, BaseModel
from uuid import UUID, uuid4

from app.domain.data.region import RegionProps, CreateRegionProps
from app.shared.domain.data.page import PageRequestDTO

from typing import Annotated

class CreateRegionDTO(CreateRegionProps):
    pass

class RegionResponseDTO(RegionProps):
    pass