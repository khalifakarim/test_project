from rest_framework.routers import DefaultRouter
from django.urls import path

from client.views import (
    UserUpdateViewSet,
    UserViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('update', UserUpdateViewSet)
router.register('', UserViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
