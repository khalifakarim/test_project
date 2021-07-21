from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("client.urls")),
    path("providers/", include("provider.urls")),
    path("showrooms/", include("car_dealerships.urls")),
]
