from rest_framework import viewsets

from core.views.mixins.base import SoftDeleteMixin, SerializerChooseMixin, SerializerChooseMixin2

from provider.serializers import (
    ProviderActionCreateSerializer,
    ProviderActionReadSerializer,
    ProviderCreateSerializer,
    ProviderReadSerializer,
    ManufacturerSerializer,
    CarCreateSerializer,
    CarPriceSerializer,
    CarReadSerializer,
)

from provider.models import (
    ProviderAction,
    Manufacturer,
    Provider,
    CarPrice,
    Car,
)


class ManufacturerViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet,
):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


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
    # read_only_serializer = CarReadSerializer
    # write_serializer = CarCreateSerializer


class ProviderViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet,
):
    queryset = Provider.objects.all()
    read_only_serializer = ProviderReadSerializer
    write_serializer = ProviderCreateSerializer


class CarPriceViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet,
):
    serializer_class = CarPriceSerializer
    queryset = CarPrice.objects.all()


class ProviderActionViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet,
):
    queryset = ProviderAction.objects.all()
    read_only_serializer = ProviderActionReadSerializer
    write_serializer = ProviderActionCreateSerializer
