from client.models import Offer

from django_filters import (
    NumberFilter,
    FilterSet,
)


class OfferFilter(FilterSet):
    maximum_price = NumberFilter(field_name="max_price", lookup_expr='lte')
    minimum_price = NumberFilter(field_name="max_price", lookup_expr='gte')

    class Meta:
        model = Offer
        fields = ('is_active', 'max_price', 'car__carcase')
