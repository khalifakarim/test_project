from rest_framework.routers import DefaultRouter

from car_dealerships.api.v1.views import (
    PurchaseCharacteristicsViewSet,
    CarDealershipActionViewSet,
    CarDealershipSaleViewSet,
    CarDealershipBuyViewSet,
    AvailableCarsViewSet,
    CarDealershipViewSet,
    LocationViewSet,
)

router = DefaultRouter()
router.register("purchase-characteristics", PurchaseCharacteristicsViewSet)
router.register("sale-history", CarDealershipSaleViewSet)
router.register("available-cars", AvailableCarsViewSet)
router.register("buy-history", CarDealershipBuyViewSet)
router.register("car-dealership", CarDealershipViewSet)
router.register("actions", CarDealershipActionViewSet)
router.register("location", LocationViewSet)

urlpatterns = router.urls
