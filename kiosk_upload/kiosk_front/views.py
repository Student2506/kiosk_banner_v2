"""Views to handle input from user."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kiosk_front.forms import KioskForm
from kiosk_front.models import Cinema


def index(request: HttpRequest) -> HttpResponse:
    """Present main page.

    Args:
        request: HttpRequest - main data for function

    Returns:
        HttpResponse: main page
    """
    cinemas = Cinema.object.all()
    form = KioskForm()
    return render(request, 'kiosk_front/index.html', {'cinemas': cinemas, 'form': form})
