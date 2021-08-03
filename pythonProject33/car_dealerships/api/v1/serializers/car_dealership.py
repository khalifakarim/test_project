from rest_framework import serializers

from car_dealerships.api.v1.serializers.available_cars import AvailableCarsSerializer
from core.serializers.base import SoftDeleteSerializer
from car_dealerships.models import CarDealership
from core.serializers.base import BaseSerializer
from provider.models import Car


class CarDealershipReadSerializer(serializers.ModelSerializer):
    cars = AvailableCarsSerializer(read_only=True, many=True)

    class Meta(BaseSerializer.Meta):
        model = CarDealership


class CarDealershipCreateSerializer(SoftDeleteSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealership

    def validate_preferred_characteristics(self, preferred_characteristics):
        car_characteristics = tuple(field.column for field in Car._meta.get_fields())

        if not set(preferred_characteristics.keys()).issubset(set(car_characteristics)):
            raise serializers.ValidationError("incorrect data")
        return preferred_characteristics
