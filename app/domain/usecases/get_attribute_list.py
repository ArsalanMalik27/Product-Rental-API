from app.domain.repository.db.attribute import AttributeRepository
async def get_attribute_list_usecase(attribute_repo: AttributeRepository):
    attribute_props = await attribute_repo.get_all_attributes()
    return attribute_props