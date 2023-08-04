from django.db import models
from userAuth.models import Buyer, Seller
from django.utils import timezone
# Create your models here.

## It is the Job table that contains the details of the job
class Job(models.Model):
    pickup_address = models.CharField(max_length=100)
    event_date = models.DateField(default=timezone.now)  # For date only
    event_time = models.TimeField(default=timezone.now)
    product_type = models.CharField(max_length=100)
    pickup_time = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=1000)
    delivery_time = models.CharField(max_length=100)
    delivery_pincode = models.IntegerField()
    pickup_pincode = models.IntegerField()
    ## associate it with buyer table
    created_by = models.ForeignKey(Buyer, on_delete=models.CASCADE,
                                related_name='buyers')  # models.CASCADE Means delete the job if the buyer is removed
    ## associate it with seller table
    assigned_to = models.ForeignKey(Seller, related_name='sellers', blank=True, null=True
                                    , on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='Pending')
    rating = models.IntegerField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=100, null=True)

    def __repr__(self) -> str:
        return f"Job ID: {self.id} Job Status: {self.status} Job Review: {self.review} Item Type: {self.product_type} Pickup Address: {self.pickup_address} Job Created: {self.date} Job OrderTag: {self.order_tag} Pickup Time:{self.pickup_time} Delivery Address: {self.delivery_address} Delivery Time: {self.delivery_time} Delivery Pincode: {self.delivery_pincode} Pickup Pincode: {self.pickup_pincode} Created By: {self.created_by} Assigned_To: {self.assigned_to}"
