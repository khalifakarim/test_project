from provider.models import CarPrice

from django_filters import (
    NumberFilter,
    FilterSet,
)


class CarPriceFilter(FilterSet):
    min_price = NumberFilter(field_name="production_year", lookup_expr='lte')
    max_price = NumberFilter(field_name="production_year", lookup_expr='gte')

    class Meta:
        model = CarPrice
        fields = ('is_active', 'price')
