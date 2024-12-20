from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from users.views import UsersListAPIView, PaymentsListAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path("users/", UsersListAPIView.as_view(), name="users-list"),
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
]#+router.urls
