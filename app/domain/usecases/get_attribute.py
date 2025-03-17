from app.domain.repository.db.attribute import AttributeRepository
from uuid import UUID

async def get_attribute_usecase(attribute_id: UUID, attribute_repo: AttributeRepository):
    attribute_props = await attribute_repo.get_by_id(attribute_id)
    return attribute_props