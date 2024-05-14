from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserForm
from .models import UserProfile


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile_page")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(
        request,
        "userprofile/edit_profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


@login_required
def profile_page(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )
    return render(
        request,
        "userprofile/profile_page.html",
        {"user_profile": user_profile},
    )
