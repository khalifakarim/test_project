from django.contrib import admin

from provider.models import (
    RegularProviderCustomers,
    ProviderAction,
    Manufacturer,
    Provider,
    CarPrice,
    Car,

)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "carcase",
        "state",
        "price",
    )
    list_filter = (
        "manufacturer__name",
        "model",
    )
    search_fields = (
        "manufacturer__name",
        "model",
    )


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "foundation_time",
    )
    list_filter = (
        "car",
        "is_active",
        "customers",
    )
    search_fields = (
        "name",
        "cars__model",
        "cars__state",
        "cars__manufacturer__name",
    )


@admin.register(ProviderAction)
class ProviderActionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "action_start_time",
        "action_end_time",
        "discount_percentage",
    )
    list_filter = (
        "cars",
        "is_active",
        "provider",
    )
    search_fields = (
        "title",
        "cars__model",
        "cars__manufacturer__name"
        "provider__name",
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "foundation_time",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(CarPrice)
class CarPriceAdmin(admin.ModelAdmin):
    list_display = (
        "provider",
        "price",
        "car",
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "provider__name"
        "car__manufacturer__name",
        "car__model",
        "car__state",
        "car__carcase",
    )


@admin.register(RegularProviderCustomers)
class RegularProviderCustomersAdmin(admin.ModelAdmin):
    list_display = (
        "provider",
        "customer",
        "discount_percentage",
        "cars_quantity",
    )
    list_filter = (
        "provider__name",
        "customer__name",
        "discount_percentage",

    )
    search_fields = (
        "provider__name",
        "customer__name",
        "discount_percentage",
    )
