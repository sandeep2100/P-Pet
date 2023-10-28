from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("logout/", logout_page, name="logout"),
    path("forget-password/", ForgotPassword, name="forget_password"),
    path("change-password/<token>/", ChangePassword, name="change_password"),

]

