from car_dealerships.models import CarDealershipSale

from django_filters import (
    NumberFilter,
    FilterSet,
)


class CarDealershipSaleFilter(FilterSet):
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    min_price = NumberFilter(field_name="price", lookup_expr='gte')

    class Meta:
        model = CarDealershipSale
        fields = ('is_active', 'price')
