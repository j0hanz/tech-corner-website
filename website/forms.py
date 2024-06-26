from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for creating a new post.
    """

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the title here..."}
        ),
        label="Title",
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 7,
                "cols": 32,
                "placeholder": "Write your post here...",
            }
        ),
        label="Body",
    )

    class Meta:
        model = Post
        fields = ["title", "body"]


class EditPostForm(forms.ModelForm):
    """
    Form for editing an existing post.
    """

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 7,
                "cols": 32,
                "placeholder": "Edit your post here...",
            }
        ),
        label="Body",
    )

    class Meta:
        model = Post
        fields = ["body"]


class CommentForm(forms.ModelForm):
    """
    Form for creating a new comment on a post.
    """

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "comment-textarea",
                "placeholder": "Write your comment here...",
            }
        ),
        label="Comment",
    )

    class Meta:
        model = Comment
        fields = ["body"]
