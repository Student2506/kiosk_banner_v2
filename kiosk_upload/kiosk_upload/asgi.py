"""ASGI config for kiosk_upload project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiosk_upload.settings')
application = get_asgi_application()
