"""kiosk_upload URL Configuration."""

from django.contrib import admin
from django.urls import path

from kiosk_front import views as kf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', kf_views.index, name='kiosk-index'),
]
