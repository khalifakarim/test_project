from rest_framework import viewsets

from provider.api.v1.serializers import ManufacturerSerializer
from core.views.mixins.base import SoftDeleteMixin
from provider.models import Manufacturer


class ManufacturerViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet,
):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    filterset_fields = ('is_active',)
    search_fields = (
        'name',
        'foundation_time',
        'location__country',
        'location__city',
    )
    ordering_fields = (
        'name',
        'foundation_time',
        'location__country',
        'location__city',
    )
