from rest_framework import serializers

from car_dealerships.api.v1.serializers.car_dealership import CarDealershipCreateSerializer
from provider.api.v1.serializers.car import CarReadSerializer
from car_dealerships.models import CarDealershipAction
from core.serializers.base import SoftDeleteSerializer
from core.serializers.base import BaseSerializer


class CarDealershipActionReadSerializer(serializers.ModelSerializer):
    car_dealership = CarDealershipCreateSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealershipAction


class CarDealershipActionCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealershipAction
