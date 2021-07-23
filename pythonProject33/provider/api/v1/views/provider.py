from rest_framework import viewsets

from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin
from provider.api.v1.serializers.provider import ProviderReadSerializer, ProviderCreateSerializer
from provider.models import Provider



class ProviderViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet,
):
    queryset = Provider.objects.all()
    read_only_serializer = ProviderReadSerializer
    write_serializer = ProviderCreateSerializer
