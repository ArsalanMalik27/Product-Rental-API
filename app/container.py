from dependency_injector import containers, providers
from app.infra.config import settings
from app.shared.infra.database import get_db

from app.repository.db.product import ProductDBRepository
from app.repository.db.attribute import AttributeDBRepository
from app.repository.db.region import RegionDBRepository
from app.repository.db.rental_period import RentalPeriodDBRepository
from app.repository.db.attribute_values import AttributeValuesDBRepository
from app.repository.db.product_pricing import ProductPricingDBRepository

class Container(containers.DeclarativeContainer):
    db_pool = providers.Resource(get_db)

    product_db_repository = providers.Factory(
        ProductDBRepository, db_session=db_pool
    )
    attribute_db_repository = providers.Factory(
        AttributeDBRepository, db_session=db_pool
    )
    region_db_repository = providers.Factory(
        RegionDBRepository, db_session=db_pool
    )
    rental_period_db_repository = providers.Factory(
        RentalPeriodDBRepository, db_session=db_pool
    )
    attribute_values_db_repository = providers.Factory(
        AttributeValuesDBRepository, db_session=db_pool
    )
    product_pricing_db_repository = providers.Factory(
        ProductPricingDBRepository, db_session=db_pool
    )
