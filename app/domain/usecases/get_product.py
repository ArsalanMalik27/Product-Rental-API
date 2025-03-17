from app.api.v1.dto.product import GetProductRequestDTO
from app.domain.repository.db.product import ProductRepository
from uuid import UUID

async def get_product_usecase(product_id: UUID, product_repo: ProductRepository):
    product_props = await product_repo.get_by_id(product_id)
    return product_props