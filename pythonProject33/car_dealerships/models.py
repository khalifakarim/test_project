from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField
from django.db import models

from provider.models import Car, SoftDelete, CreatedAt, UpdateAt
from core.enums import Carcase


class Location(models.Model):
    country = CountryField()
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    building_number = models.IntegerField()

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
    customers = models.ManyToManyField("client.User")

    def __str__(self):
        return self.name


class CarDealershipSale(SoftDelete, CreatedAt, UpdateAt):
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
    sale_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sold_car


class CarDealershipBuy(SoftDelete, CreatedAt, UpdateAt):
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


class CarDealershipAction(SoftDelete, CreatedAt, UpdateAt):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    cars = models.ManyToManyField(Car)
    car_dealership = models.ForeignKey(
        CarDealership,
        on_delete=models.SET_NULL,
        related_name="action",
        null=True,
    )
    action_start_time = models.DateTimeField()
    action_end_time = models.DateTimeField()
    discount_percentage = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.title
