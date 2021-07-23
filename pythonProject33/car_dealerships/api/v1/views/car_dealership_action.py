from rest_framework import viewsets

from core.views.mixins.base import SerializerChooseMixin
from core.views.mixins.base import SoftDeleteMixin
from car_dealerships.models import CarDealershipAction

from car_dealerships.api.v1.serializers.car_dealership_action import (
    CarDealershipActionReadSerializer,
    CarDealershipActionCreateSerializer,
)


class CarDealershipActionViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet
):
    queryset = CarDealershipAction.objects.all()
    read_only_serializer = CarDealershipActionReadSerializer
    write_serializer = CarDealershipActionCreateSerializer
