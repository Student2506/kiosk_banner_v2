"""Describe Users App settings."""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users application settings."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
