"""This module contains the urls for the Buyer App."""
from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.index, name="index"),
    path("add_job/", views.add_job, name="add_job"),
    path("my_orders/", views.my_orders, name="my_orders"),
    path("check_order/", views.check_order, name="check_order"),
    path("get_otp/", views.get_otp, name="get_otp"),
    path("completed_jobs/", views.completed_orders,
        name="buyer_completed_jobs"),
    path("thank_you/", views.thank_you, name="thank_you"),
]
