from rest_framework import viewsets, mixins

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


class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class CarPriceViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CarPriceSerializer
    queryset = CarPrice.objects.all()


class ProviderActionViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderActionSerializer
    queryset = ProviderAction.objects.all()
