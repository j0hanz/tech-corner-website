from django.urls import path
from . import views

urlpatterns = [
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("profile/", views.profile_page, name="profile_page"),
]
