"""WSGI config for kiosk_upload project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiosk_upload.settings')
application = get_wsgi_application()
