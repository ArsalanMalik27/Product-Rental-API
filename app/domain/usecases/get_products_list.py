from app.api.v1.dto.product import GetProductRequestDTO
from app.domain.repository.db.product import ProductRepository
from uuid import UUID

async def get_products_list_usecase(product_repo: ProductRepository, get_product_request_dto: GetProductRequestDTO):
    products = await product_repo.get_all_products(
        get_product_request_dto.region_id, 
        get_product_request_dto.rental_period_id, 
        get_product_request_dto.page, 
        get_product_request_dto.page_size
        )
    return products