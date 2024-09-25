from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from tech_corner.utils import shortnaturaltime


class Post(models.Model):
    """Model for Post."""

    STATUS = ((0, 'Draft'), (1, 'Published'))

    title = models.CharField(max_length=50, unique=True)  # Title
    image = CloudinaryField('image', blank=True, null=True)  # Image
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Slug
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_posts',
    )  # Author
    body = models.TextField()  # Body
    date = models.DateTimeField(auto_now_add=True)  # Date
    status = models.IntegerField(
        choices=STATUS,
        default=1,
    )  # Status (Default "Published")
    excerpt = models.TextField(
        blank=True,
    )  # Excerpt (Only available in admin interface)
    updated_on = models.DateTimeField(
        auto_now=True,
    )  # Date the post was last updated

    class Meta:
        """Meta options for the Post model."""

        ordering = ['-date']  # Orders posts by date in descending order

    def __str__(self) -> str:
        return f'{self.title} | written by {self.author}'

    @property
    def short_date(self):
        return shortnaturaltime(self.date)


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
def save_post_receiver(sender, instance, *args, **kwargs) -> None:
    """Signal to generate a slug before saving the Post."""
    if not instance.slug:
        instance.slug = unique_slug(instance)
