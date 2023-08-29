"""This file contains all the models for the Buyer App."""
from django.db import models
from django.utils import timezone
from userAuth.models import Buyer, Seller




class Job(models.Model):
    """Job table that contains the details of the job."""

    pickup_address = models.CharField(max_length=100)
    event_date = models.DateField(default=timezone.now)  # For date only
    event_time = models.TimeField(default=timezone.now)
    product_type = models.CharField(max_length=100)
    pickup_time = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=1000)
    delivery_date = models.CharField(max_length=100)
    pickup_date = models.CharField(max_length=100)
    delivery_time = models.CharField(max_length=100)
    delivery_pincode = models.IntegerField()
    pickup_pincode = models.IntegerField()
    # associate it with buyer table
    created_by = models.ForeignKey(
        Buyer, on_delete=models.CASCADE, related_name="buyers"
    )  # models.CASCADE Means delete the job if the buyer is removed
    # associate it with seller table
    assigned_to = models.ForeignKey(
        Seller, related_name="sellers", blank=True, null=True, 
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=100, default="Pending")
    rating = models.IntegerField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=100, null=True)

    def __repr__(self) -> str:
         """Return a string representation of the object."""
         return (
            f"Job ID: {self.id} Job Status: {self.status}" 
            f"Job Review: {self.review} Item Type: {self.product_type}"
            f"Pickup Address: {self.pickup_address}" 
            f"Job Created: {self.event_date} {self.event_time}"
            f"Pickup Time:{self.pickup_time}" 
            f"Delivery Address: {self.delivery_address}"
            f"Delivery Time: {self.delivery_time}" 
            f"Delivery Pincode: {self.delivery_pincode}"
            f"Pickup Pincode: {self.pickup_pincode}"
            f"Created By: {self.created_by} Assigned_To: {self.assigned_to}"
         )
