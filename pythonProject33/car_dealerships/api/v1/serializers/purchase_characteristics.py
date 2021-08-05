from rest_framework import serializers

from car_dealerships.api.v1.serializers.car_dealership import CarDealershipCreateSerializer
from provider.api.v1.serializers.provider import ProviderReadSerializer
from provider.api.v1.serializers.car import CarReadSerializer
from car_dealerships.models import PurchaseCharacteristics
from core.serializers.base import BaseSerializer


class PurchaseCharacteristicsSerializer(serializers.ModelSerializer):
    car_dealership = CarDealershipCreateSerializer(read_only=True)
    provider = ProviderReadSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = PurchaseCharacteristics
