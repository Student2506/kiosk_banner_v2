"""Models to describe kiosks."""

import uuid
from typing import Any

from django.db import models
from django.utils.translation import gettext_lazy as _

FIELD_LEN = 45


class Kiosk(models.Model):
    """Class to desribe Kiosk model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        _('Kiosk name'), max_length=FIELD_LEN, blank=False, null=False, unique=True,
    )
    short_name = models.CharField(
        _('Kiosk short name'), max_length=FIELD_LEN, blank=False, null=False, unique=True,
    )
    ip = models.GenericIPAddressField('IP адрес киоска', blank=True, null=True)
    cinema = models.ForeignKey(
        'Cinema', related_name='kiosks', on_delete=models.SET_NULL, null=True,
    )
    is_enabled = models.BooleanField(
        _('Enabled'), blank=False, null=False, default=True,
    )
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        """General Meta Class for Kiosk."""

        verbose_name = _('Kiosk')
        verbose_name_plural = _('Kiosks')
        ordering = ('name', )

    def __str__(self) -> str:
        """Return kiosk name in admin.

        Returns:
            str - name of Kiosk
        """
        return str(self.name[:FIELD_LEN])

    def save(self, *args: list[Any], **kwargs: dict[Any, Any]) -> None:
        """Save short_name in auto mode.

        Args:
            args: list[Any] - list of args
            kwargs: dict[Any, Any] - dict of kwargs
        """
        self.short_name = self.name.split('.')[0]
        super().save(*args, **kwargs)


class Cinema(models.Model):
    """Class to describe cinema."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        _('Cinema name'), max_length=FIELD_LEN, blank=False, null=False,
    )
    city = models.CharField(
        _('City'), max_length=FIELD_LEN,
    )
    slug = models.SlugField(
        'Slug', max_length=FIELD_LEN, allow_unicode=True,
    )

    class Meta:
        """General Meta Class for Cinema."""

        verbose_name = _('Cinema')
        verbose_name_plural = _('Cinemas')
        ordering = ('name', )

    def __str__(self) -> str:
        """Return Cinema name with City.

        Returns:
            str - name of kiosk with city
        """
        return str(f'{self.name} ({self.city})')
