from rest_framework import viewsets
from rest_framework import mixins

from car_dealerships.api.v1.serializers import PurchaseCharacteristicsSerializer
from car_dealerships.models import PurchaseCharacteristics
from core.views.mixins.base import SoftDeleteMixin


class PurchaseCharacteristicsViewSet(
    SoftDeleteMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PurchaseCharacteristicsSerializer
    queryset = PurchaseCharacteristics.objects.all()
