from django.db.models import signals
from django.dispatch import receiver

from car_dealerships.api.v1.services.purchase_characteristics_logic import get_better_providers
from car_dealerships.api.v1.services.available_cars_logic import create_carshowroom_cars
from car_dealerships.models import CarDealership, AvailableCars
from provider.models import Car


@receiver(signals.post_save, sender=CarDealership)
def create_available_cars(sender, instance, created, **kwargs):
    if created:
        cars = Car.objects.filter(**instance.preferred_characteristics)
        create_carshowroom_cars(cars, instance)


@receiver(signals.post_save, sender=CarDealership)
def create_purchase_characteristics(sender, instance, created, **kwargs):
    if created:
        available_cars = AvailableCars.objects.filter(car_dealership=instance)
        get_better_providers(available_cars, instance)
