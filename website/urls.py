from django.urls import path
from .views import home, PostList, about, create_post, post_detail, edit_post, lockout_view

urlpatterns = [
    path('', home, name='home'),
    path('index/', PostList.as_view(), name='index'),
    path('edit-post/<int:post_id>/', edit_post, name='edit_post'),
    path('posts/<slug:slug>/', post_detail, name='post_detail'),
    path('create-post/', create_post, name='create_post'),
    path('about/', about, name='about'),
    path('lockout/', lockout_view, name='lockout'),
]