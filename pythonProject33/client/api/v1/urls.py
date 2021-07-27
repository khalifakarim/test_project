from rest_framework.routers import DefaultRouter
from django.urls import path

from client.api.v1.views.customer import UserViewSet, UserUpdateViewSet
from client.api.v1.views.offer import OfferViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("update", UserUpdateViewSet)
router.register("offer", OfferViewSet)

urlpatterns = [
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls
