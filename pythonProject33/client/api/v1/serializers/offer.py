from rest_framework import serializers

from client.api.v1.serializers.customer import UserSerializer
from provider.api.v1.serializers.car import CarReadSerializer
from core.serializers.base import SoftDeleteSerializer
from django.db.models import Sum
from client.models import Offer


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


class OfferCreateSerializer(SoftDeleteSerializer):
    class Meta:
        model = Offer
        fields = (
            'user',
            'car',
            'max_price',
        )

    def validate_max_price(self, max_price):
        user = self.context['request'].user
        active_offers = Offer.objects.check_user_offer(user_id=user.id)
        total_price = active_offers.aggregate(total_price=Sum('max_price'))['total_price'] or 0

        if (total_price + max_price) > user.balance:
            raise serializers.ValidationError(
                {
                    "max_price": "you have not enough money "
                }
            )
        return max_price
