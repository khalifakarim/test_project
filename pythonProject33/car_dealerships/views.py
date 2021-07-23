from rest_framework import viewsets, mixins
from core.views.mixins.base import SoftDeleteMixin

from core.views.mixins.base import SerializerChooseMixin

from car_dealerships.models import (
    CarDealershipAction,
    CarDealershipSale,
    CarDealershipBuy,
    CarDealership,
    AvailableCars,
    Location,
)

from car_dealerships.serializers import (
    CarDealershipActionCreateSerializer,
    CarDealershipActionReadSerializer,
    CarDealershipCreateSerializer,
    CarDealershipReadSerializer,
    CarDealershipSaleSerializer,
    CarDealershipBuySerializer,
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
    SerializerChooseMixin,
    viewsets.ModelViewSet
):
    queryset = CarDealership.objects.all()
    read_only_serializer = CarDealershipReadSerializer
    write_serializer = CarDealershipCreateSerializer


class AvailableCarsViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = AvailableCarsSerializer
    queryset = AvailableCars.objects.all()


class CarDealershipSaleViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = CarDealershipSaleSerializer
    queryset = CarDealershipSale.objects.all()


class CarDealershipBuyViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = CarDealershipBuySerializer
    queryset = CarDealershipBuy.objects.all()


class CarDealershipActionViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet
):
    queryset = CarDealershipAction.objects.all()
    read_only_serializer = CarDealershipActionReadSerializer
    write_serializer = CarDealershipActionCreateSerializer
