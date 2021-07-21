from rest_framework.routers import SimpleRouter

from provider.views import (
    CRUDManufacturer,
    CRUDCar,
    CRUDProvider,
    CRUDCarPrice,
    CRUDProviderAction,
)

router = SimpleRouter()
router.register("manufacturer", CRUDManufacturer)
router.register("cars", CRUDCar)
router.register("providers", CRUDProvider)
router.register("car-price", CRUDCarPrice)
router.register("action", CRUDProviderAction)
urlpatterns = [] + router.urls
