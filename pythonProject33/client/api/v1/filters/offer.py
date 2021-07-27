from client.models import Offer

from django_filters import (
    NumberFilter,
    FilterSet,
)


class OfferFilter(FilterSet):
    min_price = NumberFilter(field_name="max_price", lookup_expr='lte')

    class Meta:
        model = Offer
        fields = ('is_active', 'max_price', 'car__carcase')
