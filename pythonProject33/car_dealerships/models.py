from django_countries.fields import CountryField
from django.db import models

from car_dealerships.api.v1.services.create_available_cars import create_available_cars
from core.abstract_models.abstract_models import BaseCarRelation, CarDealershipDeal
from core.abstract_models.abstract_models import Action
from provider.models import Car

from core.abstract_models.base_abstract_models import (
    SoftDelete,
    CreatedAt,
    UpdateAt,
)


class Location(models.Model):
    country = CountryField()
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    building_number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("country", "city", "street", "building_number")

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.building_number}"


class CarDealershipManager(models.Manager):

    def get_active_showrooms(self):
        return super().get_queryset().filter(is_active=True)


class CarDealership(SoftDelete, CreatedAt, UpdateAt):
    name = models.CharField(max_length=150, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name="+", null=True
    )
    preferred_characteristics = models.JSONField()
    customers = models.ManyToManyField(
        "client.User",
        related_name="car_dealerships",
    )
    providers = models.ManyToManyField(
        'provider.Provider',
        through='PurchaseCharacteristics',
        through_fields=('provider', 'car_dealership'),
    )

    objects = CarDealershipManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(CarDealership, self).save(*args, **kwargs)
        create_available_cars(self)


class PurchaseCharacteristics(SoftDelete, CreatedAt, UpdateAt):
    provider = models.ForeignKey('provider.Provider', on_delete=models.CASCADE, related_name='+')
    car_dealership = models.ForeignKey(CarDealership, on_delete=models.CASCADE, related_name='+')
    car = models.ForeignKey('provider.Car', on_delete=models.CASCADE)
    preferred_cars_quantity = models.SmallIntegerField()


class AvailableCars(SoftDelete, CreatedAt, UpdateAt, BaseCarRelation):
    cars_quantity = models.PositiveSmallIntegerField()
    car_dealership = models.ForeignKey(
        CarDealership,
        on_delete=models.CASCADE,
        related_name='cars',
    )

    def __str__(self):
        return f'{self.car_dealership} - {self.car}'


class CarDealershipSale(SoftDelete, CreatedAt, UpdateAt, CarDealershipDeal):
    customer = models.ForeignKey(
        "client.User",
        on_delete=models.SET_NULL,
        related_name="purchases",
        null=True,
    )
    car_dealership = models.ForeignKey(
        CarDealership, on_delete=models.CASCADE, related_name="sales"
    )

    def __str__(self):
        return f'{self.car} - {self.customer} - {self.car_dealership}'


class CarDealershipBuy(SoftDelete, CreatedAt, UpdateAt, CarDealershipDeal):
    cars_quantity = models.PositiveSmallIntegerField()
    car_dealership = models.ForeignKey(
        CarDealership, on_delete=models.CASCADE, related_name="purchases"
    )
    provider = models.ForeignKey(
        "provider.Provider",
        on_delete=models.SET_NULL,
        related_name="sales",
        null=True,
    )

    def __str__(self):
        return f'{self.car} - {self.provider} - {self.car_dealership}'


class CarDealershipAction(Action, SoftDelete, CreatedAt, UpdateAt):
    car_dealership = models.ForeignKey(
        CarDealership,
        on_delete=models.CASCADE,
        related_name="actions",
        null=True,
    )
