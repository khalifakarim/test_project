from rest_framework import serializers

from core.serializers.base import BaseSerializer

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


class CarDealershipSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealership


class AvailableCarsSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = AvailableCars


class CarDealershipSaleSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealershipSale


class CarDealershipBuySerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealershipBuy


class CarDealershipActionSerializer(serializers.ModelSerializer):
    class Meta(BaseSerializer.Meta):
        model = CarDealershipAction
