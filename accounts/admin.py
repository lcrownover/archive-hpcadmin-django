from django.contrib import admin

from .models import User, Pirg

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname", "email", "is_pi", "sponsor", "created")

@admin.register(Pirg)
class PirgAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created")
