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

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class SoftDelete(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CreatedAt(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdateAt(models.Model):
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
