from django.contrib import admin

from .models import (
    CarDealershipAction,
    CarDealershipSale,
    CarDealershipBuy,
    CarDealership,
    Location,
)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "city",
        "street",
        "building_number",
    )
    list_filter = ("country", "city",)
    search_fields = (
        "country",
        "city",
        "street",
        "building_number",
    )
    ordering = (
        "country",
        "city",
    )


@admin.register(CarDealership)
class CarDealershipAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "balance",
        "location",
        "preferred_manufacturer",
        "preferred_model",
    )
    list_filter = (
        "preferred_model",
        "preferred_manufacturer",
        "location__city",
        "is_active",
    )
    search_fields = (
        "name",
        "location__country",
        "location__city",
        "cars__manufacturer__name",
        "customers__email",
    )


@admin.register(CarDealershipSale)
class CarDealershipSaleAdmin(admin.ModelAdmin):
    list_display = (
        "car_dealership",
        "sold_car",
        "customer",
        "sale_time",
    )
    list_filter = (
        "sold_car__model",
        "sold_car__manufacturer__name",
        "car_dealership__name",
    )
    search_fields = (
        "car_dealership__name",
        "customer__email",
        "sold_car__model",
        "sold_car__manufacturer__name",
    )


@admin.register(CarDealershipBuy)
class CarDealershipBuyAdmin(admin.ModelAdmin):
    list_display = (
        "bought_car",
        "car_dealership",
        "provider",
        "creation_time",
    )
    list_filter = (
        "bought_car__model",
        "bought_car__manufacturer__name",
        "provider__name",
    )
    search_fields = (
        "provider__name",
        "bought_car__model",
        "bought_car__manufacturer__name",
    )


@admin.register(CarDealershipAction)
class CarDealershipActionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "action_start_time",
        "action_end_time",
        "discount_percentage",
    )
    list_filter = (
        "is_active",
        "title",
        "cars__model",
        "car_dealership__name",
    )
    search_fields = (
        "car_dealership__name",
        "cars__model",
        "cars__manufacturer__name",
    )
