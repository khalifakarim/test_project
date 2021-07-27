from rest_framework import viewsets

from car_dealerships.api.v1.filters import CarDealershipFilter
from core.views.mixins.base import SerializerChooseMixin
from car_dealerships.models import CarDealership
from core.views.mixins.base import SoftDeleteMixin

from car_dealerships.api.v1.serializers import (
    CarDealershipReadSerializer,
    CarDealershipCreateSerializer,
)


class CarDealershipViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet
):
    queryset = CarDealership.objects.all()
    read_only_serializer = CarDealershipReadSerializer
    write_serializer = CarDealershipCreateSerializer
    filterset_class = CarDealershipFilter
    search_fields = (
        'name',
        'location__country',
        'location__city',
        'customers__email',
    )
    ordering_fields = (
        'name',
        'location__country',
        'location__city',
        'customers__email',
    )
