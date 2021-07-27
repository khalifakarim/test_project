from rest_framework import viewsets

from car_dealerships.api.v1.serializers import LocationSerializer
from car_dealerships.models import Location


class LocationViewSet(
    viewsets.ModelViewSet,
):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    search_fields = (
        'country',
        'city',
        'street',
        'building_number',
    )
    ordering_fields = (
        'street',
        'building_number',
    )
