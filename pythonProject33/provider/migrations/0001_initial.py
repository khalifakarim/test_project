# Generated by Django 3.2.5 on 2021-07-23 10:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_dealerships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('model', models.CharField(max_length=50)),
                ('carcase', models.CharField(choices=[('SEDAN', 'sedan'), ('HATCHBACK', 'hatchback'), ('COUPE', 'coupe'), ('CABRIOLET', 'cabriolet'), ('LIMOUSINE', 'limousine')], max_length=13)),
                ('state', models.CharField(choices=[('NEW', 'new'), ('WITH_MILEAGE', 'with mileage'), ('BROKEN', 'broken'), ('TOTAL', 'total')], max_length=13)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('production_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2021)])),
                ('type_of_engine', models.CharField(choices=[('PETROL', 'petrol engine'), ('DIESEL', 'diesel engine'), ('GAS', 'gas engine'), ('ELECTRIC', 'electric engine')], max_length=15)),
                ('horse_power', models.IntegerField(validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(1600)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='provider.car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True)),
                ('foundation_time', models.DateTimeField()),
                ('cars', models.ManyToManyField(related_name='providers', through='provider.CarPrice', to='provider.Car')),
                ('customers', models.ManyToManyField(related_name='providers', to='car_dealerships.CarDealership')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProviderAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('action_start_time', models.DateTimeField()),
                ('action_end_time', models.DateTimeField()),
                ('discount_percentage', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='provider.car')),
                ('cars', models.ManyToManyField(related_name='_provider_provideraction_cars_+', to='provider.Car')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='provider.provider')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True)),
                ('foundation_time', models.DateTimeField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='car_dealerships.location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='carprice',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='provider.provider'),
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='provider.manufacturer'),
        ),
    ]
