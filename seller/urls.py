from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('job_details/', views.job_details, name='job_details'),
    path('my_orders/', views.my_orders, name='seller_orders'),
    path('complete_delivery', views.complete_delivery, name='complete_delivery'),
    path('completed_jobs/', views.completed_jobs, name='completed_jobs')

]