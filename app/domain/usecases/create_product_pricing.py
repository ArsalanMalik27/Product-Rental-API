from app.api.v1.dto.product_pricing import CreateProductPricingDTO, ProductPricingResponseDTO
from app.domain.repository.db.product_pricing import ProductPricingRepository
from app.domain.data.product_pricing import CreateProductPricingProps, ProductPricing
from app.shared.utils.error import DomainError

async def create_product_pricing_usecase(
    create_product_pricing_dto: CreateProductPricingDTO,
    product_pricing_repo: ProductPricingRepository
    ):
    if create_product_pricing_dto.price < 1:
        raise DomainError("Price should be greater than 0")
    create_product_pricing_props = CreateProductPricingProps(**create_product_pricing_dto.dict())
    product_pricing = ProductPricing.create_from_props(
        create_product_pricing_props,
        create_product_pricing_dto.product_id,
        create_product_pricing_dto.rental_period_id,
        create_product_pricing_dto.region_id
        )
    await product_pricing_repo.create(product_pricing.props)
    return product_pricing.props