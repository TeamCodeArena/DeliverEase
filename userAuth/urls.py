"""This module contains the urls for the UserAuth app."""
from django.urls import path
from . import views


urlpatterns = [
    path("buyer_signup/", views.buyer_signup, name="buyer_signup"),
    path("seller_signup/", views.seller_signup, name="seller_signup"),
    path("login/", views.login_user, name="login"),
]
