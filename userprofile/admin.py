from django.contrib import admin

from .models import FavoriteTech, UserProfile

admin.site.register(UserProfile)
admin.site.register(FavoriteTech)
