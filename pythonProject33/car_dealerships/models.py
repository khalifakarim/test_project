from django_countries.fields import CountryField
from django.db import models

from provider.models import Car, SoftDelete, CreatedAt, UpdateAt, Action
from core.enums import Carcase


class Location(models.Model):
    country = CountryField()
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    building_number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ["country", "city", "street", "building_number"]

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.building_number}"


class CarDealership(SoftDelete, CreatedAt, UpdateAt):
    name = models.CharField(max_length=150, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name="+", null=True
    )
    preferred_manufacturer = models.JSONField()
    preferred_model = models.JSONField()
    preferred_carcase = models.JSONField(choices=Carcase.choices())
    cars = models.ManyToManyField(
        Car,
        through="CarDealershipSale",
        through_fields=("car_dealership", "sold_car"),
    )
    customers = models.ManyToManyField(
        "client.User",
        related_name="car_dealerships",
    )

    def __str__(self):
        return self.name


class CarDealershipSale(SoftDelete, CreatedAt, UpdateAt):
    cars_quantity = models.PositiveSmallIntegerField()
    sold_car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name="+",
    )
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
        return self.sold_car


class CarDealershipBuy(SoftDelete, CreatedAt, UpdateAt):
    cars_quantity = models.PositiveSmallIntegerField()
    car_dealership = models.ForeignKey(
        CarDealership, on_delete=models.CASCADE, related_name="purchases"
    )
    bought_car = models.ForeignKey(
        Car, on_delete=models.SET_NULL, related_name="+", null=True
    )
    provider = models.ForeignKey(
        "provider.Provider",
        on_delete=models.SET_NULL,
        related_name="sales",
        null=True,
    )

    def __str__(self):
        return self.bought_car


class CarDealershipAction(Action, SoftDelete, CreatedAt, UpdateAt):
    car_dealership = models.ForeignKey(
        CarDealership,
        on_delete=models.SET_NULL,
        related_name="actions",
        null=True,
    )
