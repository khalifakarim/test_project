from provider.models import CarPrice

from django_filters import (
    NumberFilter,
    FilterSet,
)


class CarPriceFilter(FilterSet):
    max_price = NumberFilter(field_name="production_year", lookup_expr='lte')
    min_price = NumberFilter(field_name="production_year", lookup_expr='gte')

    class Meta:
        model = CarPrice
        fields = ('is_active', 'price')
