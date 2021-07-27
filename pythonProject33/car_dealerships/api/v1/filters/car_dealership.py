from car_dealerships.models import CarDealership

from django_filters import (
    NumberFilter,
    FilterSet,
)


class CarDealershipFilter(FilterSet):
    min_balance = NumberFilter(field_name="balance", lookup_expr='lte')
    max_balance_gte = NumberFilter(field_name="balance", lookup_expr='gte')

    class Meta:
        model = CarDealership
        fields = ('balance', 'is_active')
