from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, FavoriteTech


class UserProfileForm(forms.ModelForm):
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
    class Meta:
        model = User
        fields = ["username"]


class UserProfileBioForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={"type": "text", "rows": 5, "cols": 35})
    )

    class Meta:
        model = UserProfile
        fields = ["bio"]
