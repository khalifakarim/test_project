from car_dealerships.models import CarDealershipBuy

from django_filters import (
    NumberFilter,
    FilterSet,
)


class CarDealershipBuyFilter(FilterSet):
    min_cars_quantity = NumberFilter(field_name="cars_quantity", lookup_expr='gte')
    max_cars_quantity = NumberFilter(field_name="cars_quantity", lookup_expr='lte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    min_price = NumberFilter(field_name="price", lookup_expr='gte')

    class Meta:
        model = CarDealershipBuy
        fields = ('is_active', 'cars_quantity', 'price')
