from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField


class FavoriteTech(models.Model):
    """
    Model to store favorite technology types.
    """

    TYPE_LAPTOP = "Laptop"
    TYPE_SMARTPHONE = "Smartphone"
    TYPE_TABLET = "Tablet"
    TYPE_DESKTOP = "Desktop"
    TYPE_RASPBERRYPI = "Raspberry Pi"
    TYPE_NETWORKING = "Networking"
    TYPE_OTHER = "Other"

    TYPE_CHOICES = [
        (TYPE_LAPTOP, _("Laptop")),
        (TYPE_SMARTPHONE, _("Smartphone")),
        (TYPE_TABLET, _("Tablet")),
        (TYPE_DESKTOP, _("Desktop")),
        (TYPE_RASPBERRYPI, _("Raspberry Pi")),
        (TYPE_NETWORKING, _("Networking")),
        (TYPE_OTHER, _("Other")),
    ]

    type = models.CharField(
        max_length=50, choices=TYPE_CHOICES, verbose_name=_("Type")
    )

    class Meta:
        verbose_name = _("Favorite Technology")
        verbose_name_plural = _("Favorite Technologies")
        ordering = ["type"]

    def __str__(self):
        return self.type


class UserProfile(models.Model):
    """
    Extends base User model to include additional fields.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(
        _("First Name"), max_length=50, null=True, blank=True
    )
    last_name = models.CharField(
        _("Last Name"), max_length=50, null=True, blank=True
    )
    email = models.EmailField(
        _("Email Address"), max_length=300, unique=True, null=True, blank=True
    )
    favorite_tech = models.ForeignKey(
        FavoriteTech,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Favorite Technology"),
    )
    profile_image = CloudinaryField(_("Profile Image"), null=True, blank=True)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create or update UserProfile instance whenever a User is saved.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()
