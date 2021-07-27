from rest_framework import viewsets

from car_dealerships.api.v1.serializers.available_cars import AvailableCarsSerializer
from car_dealerships.api.v1.filters.available_cars import AvailableCarsFilter
from car_dealerships.models import AvailableCars
from core.views.mixins.base import SoftDeleteMixin


class AvailableCarsViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = AvailableCarsSerializer
    queryset = AvailableCars.objects.all()
    filterset_class = AvailableCarsFilter
    search_fields = (
        'car_dealership__name',
        'car__model',
        'car__carcase',
        'car__manufacturer__name',
    )
    ordering_fields = (
        'car_dealership__name',
        'car__model',
        'car__manufacturer__name',
    )
