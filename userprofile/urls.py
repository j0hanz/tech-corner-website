from django.urls import path
from . import views

urlpatterns = [
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("profile/", views.profile_page, name="profile_page"),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
