from django.urls import path
from . import views

urlpatterns = [
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile_page, name='profile_page'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('user-posts/', views.user_posts, name='user_posts'),
    path('profile/<str:username>/', views.view_profile, name='view_profile'),
]
