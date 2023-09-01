"""This module contains views of main app."""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="global_index"),
    path("about_us/", views.about_us, name="about_us"),
    path("get_started/", views.get_started, name="get_started"),
    path("buyer_or_seller/", views.buyer_or_seller, name="buyer_or_seller"),
    path("red_home/", views.red_home, name="redirect_home")
]
