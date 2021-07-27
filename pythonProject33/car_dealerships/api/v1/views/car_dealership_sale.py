from rest_framework import viewsets

from car_dealerships.api.v1.serializers.car_dealership_sale import CarDealershipSaleSerializer
from car_dealerships.api.v1.filters.car_dealeship_sale import CarDealershipSaleFilter
from car_dealerships.models import CarDealershipSale
from core.views.mixins.base import SoftDeleteMixin


class CarDealershipSaleViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = CarDealershipSaleSerializer
    queryset = CarDealershipSale.objects.all()
    filterset_class = CarDealershipSaleFilter
    search_fields = (
        'car_dealership__name',
        'car__model',
        'car__carcase',
        'car__manufacturer__name',
        'customer__email'
    )
    ordering_fields = (
        'car_dealership__name',
        'car__model',
        'car__manufacturer__name',
        'customer__email',
    )
