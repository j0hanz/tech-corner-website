from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from website.models import Comment, Post

from .forms import UserForm, UserProfileBioForm, UserProfileForm
from .models import UserProfile


@login_required
def view_profile(request, username):
    """Display the profile page of a user."""
    user = get_object_or_404(User, username=username)
    return render(request, 'userprofile/view_profile.html', {'user': user})


@login_required
def edit_profile(request):
    """Handle editing of the user's profile."""
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_page')
        else:
            messages.error(
                request,
                'There was an error updating your profile. Please try again.',
            )
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(
        request,
        'userprofile/edit_profile.html',
        {'user_form': user_form, 'profile_form': profile_form},
    )


@login_required
def user_posts(request):
    """Display the posts created by the logged-in user."""
    posts = Post.objects.filter(author=request.user)
    return render(request, 'userprofile/user_posts.html', {'posts': posts})


@login_required
def profile_page(request):
    """Display the profile page of the logged-in user,
    including a form to edit the bio.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        bio_form = UserProfileBioForm(request.POST, instance=user_profile)
        if bio_form.is_valid():
            bio_form.save()
            messages.success(request, 'Bio updated successfully!')
            return redirect('profile_page')
        messages.error(
            request,
            'There was an error updating your bio. Please try again.',
        )
    else:
        bio_form = UserProfileBioForm(instance=user_profile)

    return render(
        request,
        'userprofile/profile_page.html',
        {'user_profile': user_profile, 'bio_form': bio_form},
    )


@login_required
def delete_post(request, post_id):
    """Allow users to delete their posts."""
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, 'Unauthorized to delete this post')
        return redirect(reverse('index'))

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted successfully.')
        return redirect('user_posts')
    return render(request, 'userprofile/delete_post.html', {'post': post})


@login_required
def delete_comment(request, comment_id):
    """Allow users to delete their comments."""
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        messages.error(request, 'Unauthorized to delete this comment')
        return redirect(reverse('post_detail', args=[comment.post.slug]))

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect('post_detail', slug=comment.post.slug)
    return render(
        request,
        'userprofile/delete_comment.html',
        {'comment': comment},
    )


@login_required
def delete_account(request):
    """Allow users to delete their account."""
    if request.method == 'POST':
        user = request.user
        if user != request.user:
            messages.error(request, 'Unauthorized access')
            return redirect(reverse('index'))

        user.delete()
        messages.success(
            request,
            'Your account has been deleted successfully.',
        )
        return redirect('index')
    return render(request, 'userprofile/delete_account_confirm.html')
