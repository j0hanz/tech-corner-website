from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
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
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "Email (optional)"}),
    )

    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
            "email",
            "favorite_tech",
            "profile_image",
        ]


class UserForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username (required)",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username"]


class UserProfileBioForm(forms.ModelForm):
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "placeholder": "Describe yourself here, also please share your tech journey...",
            }
        ),
    )

    class Meta:
        model = UserProfile
        fields = ["bio"]
