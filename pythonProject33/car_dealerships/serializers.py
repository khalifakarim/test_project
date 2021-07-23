from rest_framework import serializers

from provider.serializers import CarReadSerializer, ProviderCreateSerializer
from core.serializers.base import SoftDeleteSerializer
from core.serializers.base import BaseSerializer
from client.serializers import UserSerializer

from car_dealerships.models import (
    CarDealershipAction,
    CarDealershipSale,
    CarDealershipBuy,
    CarDealership,
    AvailableCars,
    Location,
)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AvailableCarsSerializer(serializers.ModelSerializer):
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = AvailableCars


class CarDealershipReadSerializer(serializers.ModelSerializer):
    cars = AvailableCarsSerializer(read_only=True, many=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealership


class CarDealershipCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealership


class CarDealershipSaleSerializer(serializers.ModelSerializer):
    car_dealership = CarDealershipCreateSerializer(read_only=True)
    customer = UserSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealershipSale


class CarDealershipBuySerializer(serializers.ModelSerializer):
    car_dealership = CarDealershipCreateSerializer(read_only=True)
    provider = ProviderCreateSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealershipBuy


class CarDealershipActionReadSerializer(serializers.ModelSerializer):
    car_dealership = CarDealershipCreateSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealershipAction


class CarDealershipActionCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealershipAction
