from rest_framework import viewsets

from car_dealerships.api.v1.serializers.available_cars import AvailableCarsSerializer
from car_dealerships.models import AvailableCars
from core.views.mixins.base import SoftDeleteMixin


class AvailableCarsViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = AvailableCarsSerializer
    queryset = AvailableCars.objects.all()
