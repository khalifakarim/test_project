from rest_framework import viewsets

from car_dealerships.api.v1.serializers.car_dealership_buy import CarDealershipBuySerializer
from car_dealerships.models import CarDealershipBuy
from core.views.mixins.base import SoftDeleteMixin


class CarDealershipBuyViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = CarDealershipBuySerializer
    queryset = CarDealershipBuy.objects.all()
