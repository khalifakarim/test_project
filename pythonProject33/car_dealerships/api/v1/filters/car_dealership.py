from django_filters import FilterSet, NumberFilter, ChoiceFilter
from car_dealerships.models import CarDealership


class CarDealershipFilter(FilterSet):
    balance_lte = NumberFilter(field_name="balance", lookup_expr='lte')
    balance_gte = NumberFilter(field_name="balance", lookup_expr='gte')

    class Meta:
        model = CarDealership
        fields = ['balance', 'is_active']
