from rest_framework import viewsets

from car_dealerships.api.v1.serializers import AvailableCarsSerializer
from car_dealerships.api.v1.filters import AvailableCarsFilter
from core.views.mixins.base import SoftDeleteMixin
from car_dealerships.models import AvailableCars


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
