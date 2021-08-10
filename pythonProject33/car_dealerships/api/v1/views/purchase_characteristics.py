from rest_framework import viewsets, mixins

from car_dealerships.models import PurchaseCharacteristics
from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin

from car_dealerships.api.v1.serializers import (
    PurchaseCharacteristicsReadSerializer,
    PurchaseCharacteristicsCreateSerializer,
)


class PurchaseCharacteristicsViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = PurchaseCharacteristics.objects.all()
    read_only_serializer = PurchaseCharacteristicsReadSerializer
    write_serializer = PurchaseCharacteristicsCreateSerializer
