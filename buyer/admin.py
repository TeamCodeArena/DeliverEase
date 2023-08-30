"""This module registers all the Tables into the Admin Panel."""
from django.contrib import admin
from .models import Buyer, Job, Seller

# Register your models here.

admin.site.register(Buyer)
admin.site.register(Job)
admin.site.register(Seller)
