from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.contrib import messages
from .forms import PostForm, EditPostBodyForm, CommentForm


def about(request):
    return render(request, "website/about.html")


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
    Handle the display and interaction of a specific post created by a user.
    Displays all comments related to the post and sorts them by creation time.
    Allows users to submit comments on the post.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("created_on")

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully!")
            return redirect("post_detail", slug=post.slug)
        else:
            messages.error(
                request, "Error adding your comment. Please try again."
            )
    else:
        comment_form = CommentForm()

    return render(
        request,
        "website/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        },
    )


@login_required
def edit_post(request, post_id):
    """
    View to handle the editing of a post. Users can update the body of their post.
    Requires the user to be logged in.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = EditPostBodyForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(commit=False)
            post.body = form.cleaned_data["body"]
            post.save(update_fields=["body"])
            messages.success(request, "Post updated successfully!")
            return redirect("user_posts")
        else:
            messages.error(
                request, "Error updating your post. Please try again."
            )
    else:
        form = EditPostBodyForm(instance=post)

    return render(
        request, "website/edit_post.html", {"form": form, "post": post}
    )
