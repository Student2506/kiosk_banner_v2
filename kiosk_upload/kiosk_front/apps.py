"""Describe App settings."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class KioskFrontConfig(AppConfig):
    """Class to describe KioskFront APP."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kiosk_front'
    verbose_name = _('Kiosks')
