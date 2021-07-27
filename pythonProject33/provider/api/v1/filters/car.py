from django_filters import FilterSet, NumberFilter, ChoiceFilter
from provider.models import Car


class CarFilter(FilterSet):
    price_lte = NumberFilter(field_name="production_year", lookup_expr='lte')
    price_gte = NumberFilter(field_name="production_year", lookup_expr='gte')
    production_year_gte = NumberFilter(field_name="production_year", lookup_expr='gte')
    production_year_lte = NumberFilter(field_name="production_year", lookup_expr='lte')
    horse_power_lte = NumberFilter(field_name="production_year", lookup_expr='lte')
    horse_power_gte = NumberFilter(field_name="production_year", lookup_expr='gte')

    class Meta:
        model = Car
        fields = ['is_active', 'carcase', 'state', 'type_of_engine', 'production_year', 'horse_power', 'price']
