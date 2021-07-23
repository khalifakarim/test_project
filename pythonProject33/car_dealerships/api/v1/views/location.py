from rest_framework import viewsets

from car_dealerships.api.v1.serializers.location import LocationSerializer
from car_dealerships.models import Location


class LocationViewSet(
    viewsets.ModelViewSet,
):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
