from rest_framework import viewsets, mixins

from core.views.mixins.base import SoftDeleteMixin

from provider.serializers import (
    ProviderActionSerializer,
    ManufacturerSerializer,
    ProviderSerializer,
    CarPriceSerializer,
    CarSerializer,
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
    viewsets.ModelViewSet
):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class ProviderViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet,
):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class CarPriceViewSet(
    SoftDeleteMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CarPriceSerializer
    queryset = CarPrice.objects.all()


class ProviderActionViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet,
):
    serializer_class = ProviderActionSerializer
    queryset = ProviderAction.objects.all()
