from rest_framework import viewsets

from provider.api.v1.serializers.manufacturer import ManufacturerSerializer
from core.views.mixins.base import SoftDeleteMixin
from provider.models import Manufacturer


class ManufacturerViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet,
):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
