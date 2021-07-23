from rest_framework.routers import DefaultRouter

from provider.api.v1.views.provider_action import ProviderActionViewSet
from provider.api.v1.views.manufacturer import ManufacturerViewSet
from provider.api.v1.views.car_price import CarPriceViewSet
from provider.api.v1.views.provider import ProviderViewSet
from provider.api.v1.views.car import CarViewSet

router = DefaultRouter()
router.register("manufacturer", ManufacturerViewSet)
router.register("action", ProviderActionViewSet)
router.register("providers", ProviderViewSet)
router.register("car-price", CarPriceViewSet)
router.register("cars", CarViewSet)

urlpatterns = [] + router.urls
