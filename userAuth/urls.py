from django.urls import path
from . import views

## these are the url patterns for the user authorization.
urlpatterns = [
    path('buyer_signup/', views.buyer_signup, name='buyer_signup'),
    path('seller_signup/', views.seller_signup, name='seller_signup'),
    path('login/', views.login_user, name='login')
]