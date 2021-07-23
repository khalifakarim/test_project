from rest_framework import serializers

from provider.api.v1.serializers.car import CarReadSerializer
from car_dealerships.models import AvailableCars
from core.serializers.base import BaseSerializer


class AvailableCarsSerializer(serializers.ModelSerializer):
    car = CarReadSerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = AvailableCars
