from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models


class Action(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    cars = models.ManyToManyField("provider.Car", related_name='+')
    action_start_time = models.DateTimeField()
    action_end_time = models.DateTimeField()
    discount_percentage = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    car = models.ForeignKey(
        "provider.Car",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        abstract = True


class BaseCarRelation(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(
        "provider.Car",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
    )

    class Meta:
        abstract = True


class CarDealershipDeal(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(
        "provider.Car",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
    )

    class Meta:
        abstract = True


class RegularCustomers(models.Model):
    discount_percentage = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    purchase_amount = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True
