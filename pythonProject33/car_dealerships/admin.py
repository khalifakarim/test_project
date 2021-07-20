from django.contrib import admin

from car_dealerships.models import (
    CarDealershipAction,
    CarDealershipSale,
    CarDealershipBuy,
    AvailableCars,
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
    )
    list_filter = (
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
        "car",
        "customer",
        "creation_time",
    )
    list_filter = (
        "car__model",
        "car__manufacturer__name",
        "car_dealership__name",
    )
    search_fields = (
        "car_dealership__name",
        "customer__email",
        "car__model",
        "car__manufacturer__name",
    )


@admin.register(CarDealershipBuy)
class CarDealershipBuyAdmin(admin.ModelAdmin):
    list_display = (
        "car",
        "car_dealership",
        "provider",
        "creation_time",
    )
    list_filter = (
        "car__model",
        "car__manufacturer__name",
        "provider__name",
    )
    search_fields = (
        "provider__name",
        "car__model",
        "car__manufacturer__name",
    )


@admin.register(CarDealershipAction)
class CarDealershipActionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
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


@admin.register(AvailableCars)
class AvailableCarsAdmin(admin.ModelAdmin):
    list_display = (
        "cars_quantity",
        "price",
        "car",
        "car_dealership"
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "car_dealership__name"
        "car__manufacturer__name",
        "car__model",
        "car__state",
        "car__carcase",
    )
