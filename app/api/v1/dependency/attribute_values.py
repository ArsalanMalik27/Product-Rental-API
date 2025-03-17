from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Request
from app.api.v1.dto.attribute_values import CreateAttributeValuesDTO
from app.container import Container

from app.domain.usecases.get_product import get_product_usecase
from app.domain.usecases.get_attribute import get_attribute_usecase
from app.domain.data.product import ProductProps

from app.domain.repository.db.product import ProductRepository
from app.domain.repository.db.attribute import AttributeRepository
from app.shared.utils.error import DomainError

@inject
async def valid_attribute_values_dto(
    create_attribute_values_dto: CreateAttributeValuesDTO,
    product_repo: ProductRepository = Depends(
        Provide[Container.product_db_repository]
    ),
    attribute_repo: AttributeRepository = Depends(
        Provide[Container.attribute_db_repository]
    ),
) -> CreateAttributeValuesDTO:
    product_props = await get_product_usecase(create_attribute_values_dto.product_id, product_repo)
    if not product_props:
        raise DomainError("Invalid Product Id")
    attribute_props = await get_attribute_usecase(create_attribute_values_dto.attribute_id, attribute_repo)
    if not attribute_props:
        raise DomainError("Invalid Attribute Id")
    return create_attribute_values_dto