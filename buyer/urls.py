from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("add_job/", views.add_job, name="add_job"),
    path("my_orders/", views.my_orders, name="my_orders"),
    path("check_order/", views.check_order, name="check_order"),
    path("get_otp/", views.get_otp, name="get_otp"),
]

# home
# job
# home -> myorders -> check order
#


# seller
# home
# check job
#
#
# main
# index
# aboutus
