"""Admin forms for kiosks."""

from django.contrib import admin
from kiosk_front.models import Cinema, Kiosk


@admin.register(Kiosk)
class KioskAdmin(admin.ModelAdmin):
    """Kiosk Admin model."""

    empty_value_display = '-пусто-'
    list_filter = ('cinema__name', 'cinema__city')
    search_fields = ('name', 'cinema__name', 'cinema__city')


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    """Cinema Admin model."""

    search_fields = ('name', 'city')
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('name',)}
