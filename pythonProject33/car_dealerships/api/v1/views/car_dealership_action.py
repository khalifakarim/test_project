from rest_framework import viewsets

from core.views.mixins.base import SerializerChooseMixin
from car_dealerships.models import CarDealershipAction
from core.views.mixins.base import SoftDeleteMixin

from car_dealerships.api.v1.serializers import (
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
    search_fields = (
        'title',
        'car_dealership__name',
        'action_start_time',
        'action_end_time',
        'car__model',
        'car__carcase',
        'car__manufacturer__name',
    )
    ordering_fields = (
        'car_dealership__name',
        'action_start_time',
        'action_end_time',
        'car__model',
        'car__manufacturer__name',
    )
