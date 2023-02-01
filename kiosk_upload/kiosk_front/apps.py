"""Describe App settings."""

from django.apps import AppConfig


class KioskFrontConfig(AppConfig):
    """Class to describe KioskFront APP."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kiosk_front'
