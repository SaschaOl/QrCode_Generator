from django.urls import path
from .views import show_auth, show_reg, logout_user

urlpatterns = [
    path("auth/", show_auth, name = "auth"),
    path("reg/", show_reg, name = "reg"),
    path("logout/", logout_user, name = "logout")
]