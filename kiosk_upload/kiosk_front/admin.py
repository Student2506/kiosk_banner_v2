"""Admin forms for kiosks."""

from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from kiosk_front.models import Cinema, Kiosk


@admin.register(Kiosk)
class KioskAdmin(admin.ModelAdmin):
    """Kiosk Admin model."""

    empty_value_display = '-пусто-'
    list_filter = ('cinema__name', 'cinema__city')
    search_fields = ('name', 'cinema__name', 'cinema__city')
    fields = ('name', 'ip', 'cinema', 'is_enabled')


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    """Cinema Admin model."""

    search_fields = ('name', 'city')
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('name',)}


admin.site.site_header = _('Banner Management System')
admin.site.site_title = _('Banners')
admin.site.index_title = _('Welcome to Banner Management System')
admin.site.unregister(Group)
