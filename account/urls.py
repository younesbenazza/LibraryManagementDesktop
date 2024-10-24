from django.urls import path
from .views import register, current_user, update_user

urlpatterns = [
    path("register/", register, name="register"),
    path("userinfo/", current_user, name="user_info"),
    path("userinfo/update", update_user, name="update_user"),
]
