from rest_framework import serializers

from client.models import User, Offer
from provider.serializers import CarReadSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'is_active',
            'password',
            'gender',
            'age',
        )
        read_only = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class OfferReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = (
            'user',
            'car',
            'max_price',
        )


class OfferCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = (
            'user',
            'car',
            'max_price',
        )
