from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class FavoriteTech(models.Model):
    TYPE_CHOICES = [
        ("Laptop", "Laptop"),
        ("Smartphone", "Smartphone"),
        ("Tablet", "Tablet"),
        ("Other", "Other"),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.type


class UserProfile(models.Model):
    """
    Extends base User model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    email = models.EmailField(max_length=300)
    favorite_tech = models.ForeignKey(
        FavoriteTech, on_delete=models.SET_NULL, null=True, blank=True
    )
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )

    def __str__(self):
        return self.email


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
