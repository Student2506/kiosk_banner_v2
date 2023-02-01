"""Admin forms for kiosks."""

from django.contrib import admin
from kiosk_front.models import Cinema, Kiosk


@admin.register(Kiosk)
class KioskAdmin(admin.ModelAdmin):
    """Kiosk Admin model."""

    pass


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    """Cinema Admin model."""

    prepopulated_fields = {'slug': ('name',)}
