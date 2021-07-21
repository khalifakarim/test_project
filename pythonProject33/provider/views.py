from rest_framework.response import Response
from rest_framework import viewsets, status, mixins

from provider.serializers import (
    ManufacturerSerializer,
    CarSerializer,
    ProviderSerializer,
    CarPriceSerializer,
    ProviderActionSerializer,
)

from provider.models import (
    Manufacturer,
    Car,
    Provider,
    CarPrice,
    ProviderAction,
)


class CRUDManufacturer(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

    def list(self, request, *args, **kwargs):
        if len(self.queryset) == 0:
            return Response({"message": "you do not have manufacturer"},
                            status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)


class CRUDCar(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def list(self, request, *args, **kwargs):
        if len(self.queryset) == 0:
            return Response({"message": "you do not have cars"},
                            status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)


class CRUDProvider(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    def list(self, request, *args, **kwargs):
        if len(self.queryset) == 0:
            return Response({"message": "you do not have providers"},
                            status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)


class CRUDCarPrice(viewsets.ModelViewSet):
    serializer_class = CarPriceSerializer
    queryset = CarPrice.objects.all()

    def list(self, request, *args, **kwargs):
        if len(self.queryset) == 0:
            return Response({"message": "you do not have manufacturer"},
                            status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)


class CRUDProviderAction(viewsets.ModelViewSet):
    serializer_class = ProviderActionSerializer
    queryset = ProviderAction.objects.all()

    def list(self, request, *args, **kwargs):
        if len(self.queryset) == 0:
            return Response({"message": "you do not have manufacturer"},
                            status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)
