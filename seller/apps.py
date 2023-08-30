"""App Config for seller app."""
from django.apps import AppConfig


class SellerConfig(AppConfig):
    """Main Configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "seller"
