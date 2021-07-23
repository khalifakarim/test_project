from rest_framework import viewsets

from car_dealerships.api.v1.serializers.car_dealership_sale import CarDealershipSaleSerializer
from car_dealerships.models import CarDealershipSale
from core.views.mixins.base import SoftDeleteMixin


class CarDealershipSaleViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = CarDealershipSaleSerializer
    queryset = CarDealershipSale.objects.all()
