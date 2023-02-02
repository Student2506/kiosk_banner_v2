"""Module to provide forms."""

from django import forms
from django.utils.translation import gettext_lazy as _

from kiosk_front.models import Kiosk


class KioskForm(forms.ModelForm):
    """Class to provide form for choose."""

    class Meta:
        """Generic Meta class for form."""

        model = Kiosk
        fields = ['cinema']
        labels = {
            'cinema': _('Cinema name'),
        }
