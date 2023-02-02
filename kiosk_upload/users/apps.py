"""Describe Users App settings."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """Users application settings."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = _('Users')
