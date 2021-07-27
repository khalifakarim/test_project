from rest_framework import viewsets

from provider.api.v1.serializers.car_price import CarPriceSerializer
from provider.api.v1.filters.car_price import CarPriceFilter
from core.views.mixins.base import SoftDeleteMixin
from provider.models import CarPrice


class CarPriceViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet,
):
    serializer_class = CarPriceSerializer
    queryset = CarPrice.objects.all()
    filterset_class = CarPriceFilter
    search_fields = (
        'provider__name'
        'car__manufacturer__name',
        'car__model',
    )
    ordering_fields = (
        'provider__name'
        'car__manufacturer__name',
        'car__model',
    )
