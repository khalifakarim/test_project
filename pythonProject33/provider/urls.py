from rest_framework.routers import DefaultRouter

from provider.views import (
    ProviderActionViewSet,
    ManufacturerViewSet,
    ProviderViewSet,
    CarPriceViewSet,
    CarViewSet,
)


router = DefaultRouter()
router.register("manufacturer", ManufacturerViewSet)
router.register("action", ProviderActionViewSet)
router.register("providers", ProviderViewSet)
router.register("car-price", CarPriceViewSet)
router.register("cars", CarViewSet)

urlpatterns = [] + router.urls
