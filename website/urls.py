from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create-post/', views.create_post, name='create_post'),
    path('about/', views.about, name='about'),
]
