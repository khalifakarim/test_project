# Generated by Django 3.2.5 on 2021-07-15 18:28

import core.enums
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarDealership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("creation_time", models.DateTimeField(auto_now_add=True)),
                ("modification_time", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=150, unique=True)),
                ("balance", models.DecimalField(decimal_places=2, max_digits=10)),
                ("preferred_manufacturer", models.CharField(max_length=50)),
                ("preferred_model", models.CharField(max_length=50)),
                (
                    "preferred_carcase",
                    models.CharField(
                        choices=[
                            (core.enums.Carcase["SEDAN"], "sedan"),
                            (core.enums.Carcase["HATCHBACK"], "hatchback"),
                            (core.enums.Carcase["COUPE"], "coupe"),
                            (core.enums.Carcase["CABRIOLET"], "cabriolet"),
                            (core.enums.Carcase["LIMOUSINE"], "limousine"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CarDealershipAction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("creation_time", models.DateTimeField(auto_now_add=True)),
                ("modification_time", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("action_start_time", models.DateTimeField()),
                ("action_end_time", models.DateTimeField()),
                (
                    "discount_percentage",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CarDealershipBuy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("creation_time", models.DateTimeField(auto_now_add=True)),
                ("modification_time", models.DateTimeField(auto_now=True)),
                ("purchase_time", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("city", models.CharField(max_length=150)),
                ("street", models.CharField(max_length=150)),
                ("building_number", models.IntegerField()),
            ],
            options={
                "unique_together": {("country", "city", "street", "building_number")},
            },
        ),
        migrations.CreateModel(
            name="CarDealershipSale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("creation_time", models.DateTimeField(auto_now_add=True)),
                ("modification_time", models.DateTimeField(auto_now=True)),
                ("sale_time", models.DateTimeField(auto_now_add=True)),
                (
                    "car_dealership",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sale",
                        to="car_dealerships.cardealership",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
