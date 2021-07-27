from django.urls import path, include, re_path
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("client.api.v1.urls")),
    path("providers/", include("provider.api.v1.urls")),
    path("showrooms/", include("car_dealerships.api.v1.urls")),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.extend((
        path('__debug__/', include(debug_toolbar.urls)),
    ))

if settings.SWAGGER:
    from pyhtonProject33.yasg import urlpatterns as swagger_urls

    urlpatterns.extend(swagger_urls)
