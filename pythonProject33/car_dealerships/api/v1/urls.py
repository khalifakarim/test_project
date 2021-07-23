from rest_framework.routers import DefaultRouter

from car_dealerships.api.v1.views.car_dealership_action import CarDealershipActionViewSet
from car_dealerships.api.v1.views.car_dealership_sale import CarDealershipSaleViewSet
from car_dealerships.api.v1.views.car_dealership_buy import CarDealershipBuyViewSet
from car_dealerships.api.v1.views.available_cars import AvailableCarsViewSet
from car_dealerships.api.v1.views.car_dealership import CarDealershipViewSet
from car_dealerships.api.v1.views.location import LocationViewSet

router = DefaultRouter()
router.register("sale-history", CarDealershipSaleViewSet)
router.register("available-cars", AvailableCarsViewSet)
router.register("buy-history", CarDealershipBuyViewSet)
router.register("actions", CarDealershipActionViewSet)
router.register("location", LocationViewSet)
router.register("", CarDealershipViewSet)

urlpatterns = router.urls
