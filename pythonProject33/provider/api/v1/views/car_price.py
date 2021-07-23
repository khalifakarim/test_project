from rest_framework import viewsets

from provider.api.v1.serializers.car_price import CarPriceSerializer
from core.views.mixins.base import SoftDeleteMixin
from provider.models import CarPrice



class CarPriceViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet,
):
    serializer_class = CarPriceSerializer
    queryset = CarPrice.objects.all()