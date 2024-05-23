from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]


class EditPostBodyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["body"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            'body': forms.Textarea(attrs={'class': 'comment-textarea', "placeholder": "Write your comment here..."}),
        }
