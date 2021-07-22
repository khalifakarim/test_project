from rest_framework import viewsets, mixins
from core.views.mixins.base import SoftDeleteMixin

from car_dealerships.models import (
    CarDealershipAction,
    CarDealershipSale,
    CarDealershipBuy,
    CarDealership,
    AvailableCars,
    Location,
)

from car_dealerships.serializers import (
    CarDealershipActionSerializer,
    CarDealershipSaleSerializer,
    CarDealershipBuySerializer,
    CarDealershipSerializer,
    AvailableCarsSerializer,
    LocationSerializer,
)


class LocationViewSet(
    viewsets.ModelViewSet,
):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class CarDealershipViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    serializer_class = CarDealershipSerializer
    queryset = CarDealership.objects.all()


class AvailableCarsViewSet(
    SoftDeleteMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = AvailableCarsSerializer
    queryset = AvailableCars.objects.all()


class CarDealershipSaleViewSet(
    SoftDeleteMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CarDealershipSaleSerializer
    queryset = CarDealershipSale.objects.all()


class CarDealershipBuyViewSet(
    SoftDeleteMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CarDealershipBuySerializer
    queryset = CarDealershipBuy.objects.all()


class CarDealershipActionViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet
):
    serializer_class = CarDealershipActionSerializer
    queryset = CarDealershipAction.objects.all()
