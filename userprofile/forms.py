from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A form to update a user's profile information.
    """

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name (optional)",
            }
        ),
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name (optional)",
            }
        ),
    )

    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
            "favorite_tech",
            "profile_image",
        ]


class UserForm(forms.ModelForm):
    """
    A form to update a user's username and email.
    """

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username (required)",
            }
        ),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email (optional)",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email"]


class UserProfileBioForm(forms.ModelForm):
    """
    A form to update a user's profile bio.
    """

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 32,
                "placeholder": "Describe yourself...",
            }
        ),
    )

    class Meta:
        model = UserProfile
        fields = ["bio"]
