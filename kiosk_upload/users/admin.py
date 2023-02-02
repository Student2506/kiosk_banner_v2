"""Admin module for Users app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class UserAdminCustom(UserAdmin):
    """User Admin customization."""

    pass
