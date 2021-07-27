from django_filters import FilterSet, NumberFilter, ChoiceFilter
from client.models import Offer


class OfferFilter(FilterSet):
    max_price = NumberFilter(field_name="max_price", lookup_expr='lte')

    class Meta:
        model = Offer
        fields = ['is_active', 'max_price', 'car__carcase']
