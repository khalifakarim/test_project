from django_filters import FilterSet, NumberFilter, ChoiceFilter
from provider.models import Car


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = ['is_active']
