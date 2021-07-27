from rest_framework import viewsets

from provider.api.v1.serializers import ProviderActionReadSerializer, ProviderActionCreateSerializer
from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin
from provider.api.v1.filters import ProviderActionFilter
from provider.models import ProviderAction


class ProviderActionViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet,
):
    queryset = ProviderAction.objects.all()
    read_only_serializer = ProviderActionReadSerializer
    write_serializer = ProviderActionCreateSerializer
    filterset_class = ProviderActionFilter
    search_fields = (
        'title',
        'provider__name',
        'action_start_time',
        'action_end_time',
        'car__model',
        'car__carcase',
        'car__manufacturer__name',
    )
    ordering_fields = (
        'provider__name',
        'action_start_time',
        'action_end_time',
        'car__model',
        'car__manufacturer__name',
    )
