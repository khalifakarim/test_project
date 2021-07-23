from rest_framework import serializers

from car_dealerships.api.v1.serializers.available_cars import AvailableCarsSerializer
from core.serializers.base import SoftDeleteSerializer
from car_dealerships.models import CarDealership
from core.serializers.base import BaseSerializer


class CarDealershipReadSerializer(serializers.ModelSerializer):
    cars = AvailableCarsSerializer(read_only=True, many=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealership


class CarDealershipCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealership
