from app.api.v1.dto.product import CreateProductDTO
from app.domain.repository.db.product import ProductRepository
from app.domain.data.product import Product, ProductProps, CreateProductProps
async def create_product_usecase(
    create_product_dto: CreateProductDTO, 
    product_repo: ProductRepository
    ):
    product_props = CreateProductProps(**create_product_dto.dict())
    product = Product.create_from(product_props)
    await product_repo.create_product(product.props)
    return product.props
