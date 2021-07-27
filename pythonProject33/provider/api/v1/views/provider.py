from rest_framework import viewsets

from provider.api.v1.serializers import ProviderReadSerializer, ProviderCreateSerializer
from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin
from provider.models import Provider


class ProviderViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet,
):
    queryset = Provider.objects.all()
    read_only_serializer = ProviderReadSerializer
    write_serializer = ProviderCreateSerializer
    filterset_fields = ('is_active',)
    search_fields = (
        'name',
        'foundation_time',
        'customers__name',
    )
    ordering_fields = (
        'name',
        'foundation_time',
        'customers__name',
    )
