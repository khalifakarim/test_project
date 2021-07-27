from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from drf_yasg import openapi
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("client.api.v1.urls")),
    path("providers/", include("provider.api.v1.urls")),
    path("showrooms/", include("car_dealerships.api.v1.urls")),

    re_path(r'^swagger(json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.extend((
        path('__debug__/', include(debug_toolbar.urls)),
    ))
