"""Admin forms for kiosks."""

from django.contrib import admin
from kiosk_front.models import Kiosk


@admin.register(Kiosk)
class KioskAdmin(admin.ModelAdmin):
    """Kiosk Admin model."""

    pass
