# from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = (
        "last_name",
        "username",
        "first_name",
        "email",
        "token",
        "is_active",
        "is_superuser",
    )
    list_display_links = (
        "last_name",
        "first_name",
    )
    list_filter = ["sexe", "status", "is_active", "is_staff", "is_superuser"]
    search_fields = ("last_name", "first_name", "email")
