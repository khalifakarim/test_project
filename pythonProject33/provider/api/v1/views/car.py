from rest_framework import viewsets

from provider.api.v1.serializers import CarReadSerializer, CarCreateSerializer
from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin2
from provider.api.v1.filters import CarFilter
from provider.models import Car


class CarViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin2,
    viewsets.ModelViewSet
):
    queryset = Car.objects.all()
    default_serializer_class = CarReadSerializer
    allow_serializer_class = {
        "retrieve": CarReadSerializer,
        "update": CarCreateSerializer,
        "create": CarCreateSerializer,
        "list": CarReadSerializer,
    }
    filterset_class = CarFilter
    search_fields = (
        'manufacturer__name',
        'model',
    )
    ordering_fields = (
        'manufacturer__name',
        'model',
    )
