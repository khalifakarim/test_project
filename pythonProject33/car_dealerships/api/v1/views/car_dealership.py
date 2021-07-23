from rest_framework import viewsets

from core.views.mixins.base import SerializerChooseMixin
from car_dealerships.models import CarDealership
from core.views.mixins.base import SoftDeleteMixin

from car_dealerships.api.v1.serializers.car_dealership import (
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
