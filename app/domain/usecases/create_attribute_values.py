from app.api.v1.dto.attribute_values import CreateAttributeValuesDTO
from app.domain.repository.db.attribute_values import AttributeValuesRepository
from app.domain.data.attribute_values import CreateAttributeValuesProps, AttributeValues


async def create_attribute_values_usecase(
    create_attribute_values_dto : CreateAttributeValuesDTO,
    attribute_values_repo: AttributeValuesRepository,
    ):
    create_attribute_values_props = CreateAttributeValuesProps(value=create_attribute_values_dto.value)
    attribute_values = AttributeValues.create_from_props(
        create_attribute_values_props,
        create_attribute_values_dto.attribute_id,
        create_attribute_values_dto.product_id
        )
    attribute_values.props
    await attribute_values_repo.create(attribute_values.props)
    return attribute_values.props