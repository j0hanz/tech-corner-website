from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import CommentForm, EditPostForm, PostForm
from .models import Comment, Post


class PostList(ListView):
    """Displays a paginated list of published posts.
    Sorted by their publication date in descending order.
    """

    model = Post
    template_name = 'website/index.html'
    context_object_name = 'posts'
    paginate_by = 5  # Number of posts displayed per page.
    queryset = Post.objects.filter(status=1).order_by(
        '-date',
    )  # The set of posts to display, filtered and sorted.


def home(request):
    """Serve as the entry point for the website.
    Redirecting users based on their authentication status.
    Authenticated users are redirected to the index page.
    Non-authenticated users are redirected to the About page.
    """
    if request.user.is_authenticated:
        return redirect('index')
    return redirect('about')


def lockout_view(request):
    """Renders the lockout page."""
    return render(request, 'website/lockout.html')


def about(request):
    """Renders the about page of the website."""
    return render(request, 'website/about.html')


@login_required
def create_post(request):
    """Handle the creation of a new post."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()  # Save the Post object to the database
            messages.success(request, 'You have uploaded a new Post!')
            return redirect('index')
        messages.error(
            request,
            'Error when creating a Post, please try again.',
        )
    else:
        form = PostForm()
    return render(request, 'website/create_post.html', {'form': form})


def index(request):
    """Display a list of published posts on Home page."""
    posts = Post.objects.filter(status=1).order_by('-date')
    return render(request, 'website/index.html', {'posts': posts})


def post_detail(request, slug):
    """Displays a user's post with comments."""
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-created_on')
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('post_detail', slug=post.slug)
        messages.error(
            request,
            'Error adding your comment. Please try again.',
        )
    else:
        comment_form = CommentForm()

    return render(
        request,
        'website/post_detail.html',
        {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        },
    )


@login_required
def edit_post(request, post_id):
    """View to handle the editing of a post.
    Users can update the body of their post.
    Requires the user to be logged in.
    """
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, 'Unauthorized Access')
        return redirect('index')

    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('user_posts')
        messages.error(
            request,
            'Error updating your post. Please try again.',
        )
    else:
        form = EditPostForm(instance=post)

    return render(
        request,
        'website/edit_post.html',
        {'form': form, 'post': post},
    )
