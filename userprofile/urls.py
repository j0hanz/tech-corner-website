from django.urls import path
from . import views
from .views import delete_account

urlpatterns = [
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("profile/", views.profile_page, name="profile_page"),
    path("delete-post/<int:post_id>/", views.delete_post, name="delete_post"),
    path('delete_account/', delete_account, name='delete_account'),
    path('user-posts/', views.user_posts, name='user_posts'),
    path('profile/<str:username>/', views.view_profile, name='view_profile'),
]
