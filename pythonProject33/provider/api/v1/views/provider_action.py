from rest_framework import viewsets

from provider.api.v1.serializers.provider_action import ProviderActionReadSerializer, ProviderActionCreateSerializer
from provider.api.v1.filters.provider_action import ProviderActionFilter
from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin
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
