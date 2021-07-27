from provider.models import Car

from django_filters import (
    NumberFilter,
    FilterSet,
)


class CarFilter(FilterSet):
    min_price = NumberFilter(field_name="production_year", lookup_expr='lte')
    max_price = NumberFilter(field_name="production_year", lookup_expr='gte')
    max_production_year = NumberFilter(field_name="production_year", lookup_expr='gte')
    min_production_year = NumberFilter(field_name="production_year", lookup_expr='lte')
    min_horse_power = NumberFilter(field_name="production_year", lookup_expr='lte')
    max_horse_power = NumberFilter(field_name="production_year", lookup_expr='gte')

    class Meta:
        model = Car
        fields = (
            'is_active',
            'carcase',
            'state',
            'type_of_engine',
            'production_year',
            'horse_power',
            'price',
        )
