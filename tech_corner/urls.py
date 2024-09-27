"""URL configuration for tech_corner project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('userprofile/', include('userprofile.urls')),
]
