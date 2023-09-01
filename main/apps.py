"""App Config for main app."""
from django.apps import AppConfig


class MainConfig(AppConfig):
    """Main Configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
