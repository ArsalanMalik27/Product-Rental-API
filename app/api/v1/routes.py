from fastapi import APIRouter, Depends
from app.api.v1.health import router as health_router
from app.api.v1.product import router as product_router
from app.api.v1.attribute import router as attribute_router
from app.api.v1.region import router as region_router
from app.api.v1.rental_period import router as rental_period_router
from app.api.v1.attribute_values import router as attribute_values_router
from app.api.v1.product_pricing import router as product_pricing_router

api_router = APIRouter()

api_router.include_router(region_router, prefix="/region", tags=["Region"])
api_router.include_router(rental_period_router, prefix="/rental_period", tags=["Rental Period"])
api_router.include_router(product_router, prefix="/product", tags=["Product"])
api_router.include_router(attribute_router, prefix="/attribute", tags=["Attribute"])
api_router.include_router(attribute_values_router, prefix="/attribute_values", tags=["Attribute Values"])
api_router.include_router(product_pricing_router, prefix="/product_pricing", tags=["Product Pricing"])

api_router.include_router(health_router, prefix="/health", tags=["Health"])