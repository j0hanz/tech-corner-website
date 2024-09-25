from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    """Form for creating a new post."""

    image = forms.ImageField(
        required=False,
        label='',
        widget=forms.FileInput(attrs={'class': 'form-control-file'}),
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the title here...',
                'class': 'form-control',
            },
        ),
        label='Title',
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 7,
                'cols': 32,
                'placeholder': 'Write your post here...',
                'class': 'form-control',
            },
        ),
        label='Body',
    )

    class Meta:
        model = Post
        fields = ['image', 'title', 'body']


class EditPostForm(forms.ModelForm):
    """Form for editing an existing post."""

    image = forms.ImageField(required=False, label='Image')
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 7,
                'cols': 32,
                'placeholder': 'Edit your post here...',
            },
        ),
        label='Body',
    )

    class Meta:
        model = Post
        fields = ['body', 'image']


class CommentForm(forms.ModelForm):
    """Form for creating a new comment on a post."""

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'comment-textarea',
                'placeholder': 'Write your comment here...',
            },
        ),
        label='Comment',
    )

    class Meta:
        model = Comment
        fields = ['body']
