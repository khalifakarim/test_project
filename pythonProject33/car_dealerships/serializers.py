from rest_framework import serializers

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
    class Meta:
        model = CarDealership
        exclude = ('creation_time', 'modification_time')


class AvailableCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableCars
        exclude = ('creation_time', 'modification_time')


class CarDealershipSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealershipSale
        exclude = ('creation_time', 'modification_time')


class CarDealershipBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealershipBuy
        exclude = ('creation_time', 'modification_time')


class CarDealershipActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealershipAction
        exclude = ('creation_time', 'modification_time')
