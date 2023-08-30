"""This module contains the models for the UserAuth app."""
from django.db import models


class Buyer(models.Model):
    """Model that contains the different details about the buyer."""

    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __repr__(self) -> str:
        """Return a string representation of the object."""
        return (
            f"{self.name}  {self.id} {self.email} {self.phone_no}"
            f"{self.email} {self.address}"
        )



class Seller(models.Model):
    """Model that contains the different details about the seller."""

    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=64)
    address = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

    def __repr__(self) -> str:
        """Return a string representation of the object."""
        return (
            f"{self.name}  {self.id} {self.email} {self.experience}" 
            f" {self.phone_no}  {self.address}"
        ) 

