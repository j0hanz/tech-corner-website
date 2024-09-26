from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from tech_corner.utils import shortnaturaltime


class Post(models.Model):
    """Model representing a blog post."""

    STATUS = ((0, 'Draft'), (1, 'Published'))

    title = models.CharField(max_length=50, unique=True)
    image = CloudinaryField('image', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_posts',
    )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=STATUS,
        default=1,
    )
    excerpt = models.TextField(
        blank=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        """Meta options for the Post model."""

        ordering = ['-date']

    def __str__(self) -> str:
        return f'{self.title} | written by {self.author}'

    @property
    def short_date(self):
        return shortnaturaltime(self.date)

    @property
    def short_updated_on(self):
        return shortnaturaltime(self.updated_on)


class Comment(models.Model):
    """Model for Comments."""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self) -> str:
        return f'Comment {self.body} by {self.author}'


def unique_slug(instance, new_slug=None):
    """Generate a unique slug for the post."""
    slug = new_slug or slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exists()
    if qs:
        new_slug = (
            f'{slug}-{Klass.objects.filter(slug__startswith=slug).count() + 1}'
        )
        return unique_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Post)
def save_post_receiver(sender, instance, *args, **kwargs):
    """Signal to generate a slug before saving the Post."""
    if not instance.slug:
        instance.slug = unique_slug(instance)
