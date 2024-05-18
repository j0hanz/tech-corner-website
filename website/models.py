from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_posts"
    )
    banner = CloudinaryField("image", default="logo.webp", blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


def unique_slug(instance, new_slug=None):
    slug = slugify(instance.title) if new_slug is None else new_slug
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f"{slug}-{Klass.objects.filter(slug=slug).count() + 1}"
        return unique_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Post)
def save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug(instance)
