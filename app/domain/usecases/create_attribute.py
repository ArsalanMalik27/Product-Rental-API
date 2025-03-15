from app.domain.repository.db.attribute import AttributeRepository
from app.api.v1.dto.attribute import CreateAttributeDTO
from app.domain.data.attribute import CreateAttributeProps, Attribute


async def create_attribute_usecase(
    create_attribute_dto: CreateAttributeDTO, 
    attribute_repo: AttributeRepository
    ):
    attribute_props = CreateAttributeProps(**create_attribute_dto.dict())
    attribute = Attribute.create_from_props(attribute_props)
    await attribute_repo.create(attribute.props)
    return attribute.props