"""App Config for buyer app."""
from django.apps import AppConfig


class BuyerConfig(AppConfig):
    """Main Configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "buyer"
