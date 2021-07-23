from rest_framework import serializers

from car_dealerships.api.v1.serializers.car_dealership import CarDealershipCreateSerializer
from provider.api.v1.serializers.car import CarReadSerializer
from client.api.v1.serializers.customer import UserSerializer
from car_dealerships.models import CarDealershipSale
from core.serializers.base import BaseSerializer


class CarDealershipSaleSerializer(serializers.ModelSerializer):
    car_dealership = CarDealershipCreateSerializer(read_only=True)
    customer = UserSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealershipSale
