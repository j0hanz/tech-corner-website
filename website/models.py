from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

"""
Define the status choices for the Post model
"""
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Define the Post model
    """

    title = models.CharField(max_length=200, unique=True)  # Title
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Slug
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_posts"
    )  # Author
    body = models.TextField()  # Body
    date = models.DateTimeField(auto_now_add=True)  # Date
    status = models.IntegerField(
        choices=STATUS, default=1
    )  # Status (Default "Published")
    excerpt = models.TextField(
        blank=True
    )  # Excerpt (Only available in admin interface)
    updated_on = models.DateTimeField(
        auto_now=True
    )  # Date the post was last updated

    class Meta:
        """
        Meta options for the Post model
        """

        ordering = ["-date"]  # Orders posts by date in descending order

    def __str__(self):
        return f"{self.title} | written by {self.author}"


def unique_slug(instance, new_slug=None):
    """
    Generate a unique slug for the post
    """
    slug = slugify(instance.title) if new_slug is None else new_slug
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f"{slug}-{Klass.objects.filter(slug=slug).count() + 1}"
        return unique_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Post)
def save_post_receiver(sender, instance, *args, **kwargs):
    """
    Signal to generate a slug before saving the Post
    """
    if not instance.slug:
        instance.slug = unique_slug(instance)
