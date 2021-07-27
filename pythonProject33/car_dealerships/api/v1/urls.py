from rest_framework.routers import DefaultRouter

from car_dealerships.api.v1.views import (
    CarDealershipActionViewSet,
    CarDealershipSaleViewSet,
    CarDealershipBuyViewSet,
    AvailableCarsViewSet,
    CarDealershipViewSet,
    LocationViewSet,
)


router = DefaultRouter()
router.register("sale-history", CarDealershipSaleViewSet)
router.register("available-cars", AvailableCarsViewSet)
router.register("buy-history", CarDealershipBuyViewSet)
router.register("actions", CarDealershipActionViewSet)
router.register("location", LocationViewSet)
router.register("car-dealership", CarDealershipViewSet)

urlpatterns = router.urls
