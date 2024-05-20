from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib import messages
from .forms import PostForm


@login_required
def create_post(request):
    """
    Handle the creation of a new post. Only accessible to logged-in users.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()  # Save the Post object to the database
            messages.success(request, "You have uploaded a new Post!")
            return redirect("index")
        else:
            messages.error(
                request,
                "Error when creating a Post, please try again.",
            )
    else:
        form = PostForm()
    return render(request, "website/create_post.html", {"form": form})


def index(request):
    """
    Display a list of published posts on Home page.
    """
    posts = Post.objects.filter(status=1).order_by("-date")
    return render(request, "website/index.html", {"posts": posts})


def post_detail(request, slug):
    """
    Display the details of a post.
    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, "website/post_detail.html", {"post": post})
