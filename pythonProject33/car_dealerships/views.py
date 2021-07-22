from rest_framework import viewsets, mixins

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


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class CarDealershipViewSet(viewsets.ModelViewSet):
    serializer_class = CarDealershipSerializer
    queryset = CarDealership.objects.all()


class AvailableCarsViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = AvailableCarsSerializer
    queryset = AvailableCars.objects.all()


class CarDealershipSaleViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    serializer_class = CarDealershipSaleSerializer
    queryset = CarDealershipSale.objects.all()


class CarDealershipBuyViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    serializer_class = CarDealershipBuySerializer
    queryset = CarDealershipBuy.objects.all()


class CarDealershipActionViewSet(viewsets.ModelViewSet):
    serializer_class = CarDealershipActionSerializer
    queryset = CarDealershipAction.objects.all()
