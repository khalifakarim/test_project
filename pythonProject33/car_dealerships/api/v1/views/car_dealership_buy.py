from rest_framework import viewsets

from car_dealerships.api.v1.serializers import CarDealershipBuySerializer
from car_dealerships.api.v1.filters import CarDealershipBuyFilter
from car_dealerships.models import CarDealershipBuy
from core.views.mixins.base import SoftDeleteMixin


class CarDealershipBuyViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = CarDealershipBuySerializer
    queryset = CarDealershipBuy.objects.all()
    filterset_class = CarDealershipBuyFilter
    search_fields = (
        'car_dealership__name',
        'provider__name',
        'car__model',
        'car__carcase',
        'car__manufacturer__name',
    )
    ordering_fields = (
        'car_dealership__name',
        'provider__name',
        'car__model',
        'car__manufacturer__name',
    )
