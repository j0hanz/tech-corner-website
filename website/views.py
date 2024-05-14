from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.filter(status=1).order_by("-date")
    return render(request, "website/index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "website/post_detail.html", {"post": post})
