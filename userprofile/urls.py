from django.urls import path
from . import views
from .views import delete_account

urlpatterns = [
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("profile/", views.profile_page, name="profile_page"),
    path('delete_account/', delete_account, name='delete_account'),
    path('user-posts/', views.user_posts, name='user_posts'),
]
