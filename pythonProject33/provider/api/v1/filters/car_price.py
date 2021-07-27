from django_filters import FilterSet, NumberFilter, ChoiceFilter
from provider.models import CarPrice


class CarPriceFilter(FilterSet):
    price_lte = NumberFilter(field_name="production_year", lookup_expr='lte')
    price_gte = NumberFilter(field_name="production_year", lookup_expr='gte')

    class Meta:
        model = CarPrice
        fields = ['is_active', 'price']
