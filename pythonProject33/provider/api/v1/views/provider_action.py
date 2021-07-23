from rest_framework import viewsets

from provider.api.v1.serializers.provider_action import ProviderActionReadSerializer, ProviderActionCreateSerializer
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
