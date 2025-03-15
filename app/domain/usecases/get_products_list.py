from app.domain.repository.db.product import ProductRepository

async def get_products_list_usecase(product_repo: ProductRepository):
    products = await product_repo.get_all_products()
    return products