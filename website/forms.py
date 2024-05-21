from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]


class EditPostBodyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["body"]
