from rest_framework import serializers

from car_dealerships.api.v1.serializers.car_dealership import CarDealershipCreateSerializer
from provider.api.v1.serializers.provider import ProviderCreateSerializer
from provider.api.v1.serializers.car import CarReadSerializer
from car_dealerships.models import CarDealershipBuy
from core.serializers.base import BaseSerializer


class CarDealershipBuySerializer(serializers.ModelSerializer):
    car_dealership = CarDealershipCreateSerializer(read_only=True)
    provider = ProviderCreateSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealershipBuy
