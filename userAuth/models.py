from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phoneNo = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __repr__(self) -> str:
        return f"{self.name}  {self.id} {self.email} {self.phoneNo} {self.email} {self.address}"


class Seller(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phoneNo = models.CharField(max_length=64)
    address = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return f"{self.name}  {self.id} {self.email} {self.experience} {self.phoneNo}  {self.address}"

