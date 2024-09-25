from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class FavoriteTech(models.Model):
    """Model to store favorite technology types."""

    TYPE_CHOICES = [
        ('PC', _('PC')),
        ('Mobile', _('Mobile')),
        ('Tablet', _('Tablet')),
        ('AI', _('AI')),
        ('Raspberry Pi', _('Raspberry Pi')),
        ('Networking', _('Networking')),
        ('Other', _('Other')),
        ('Laptop', _('Laptop')),
        ('Smartphone', _('Smartphone')),
        ('Desktop', _('Desktop')),
        ('Smart Home', _('Smart Home')),
        ('Wearable', _('Wearable')),
        ('Gaming Console', _('Gaming Console')),
        ('VR', _('VR')),
        ('Drone', _('Drone')),
        ('IoT', _('IoT')),
        ('Cloud Computing', _('Cloud Computing')),
        ('Cyber Security', _('Cyber Security')),
    ]

    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        verbose_name=_('Type'),
    )

    class Meta:
        verbose_name = _('Favorite Tech')
        verbose_name_plural = _('Favorite Technologies')
        ordering = ['type']

    def __str__(self) -> str:
        return self.type


class UserProfile(models.Model):
    """Extends base User model to include additional fields."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='userprofile'
    )
    first_name = models.CharField(
        _('First Name'),
        max_length=50,
        blank=True,
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=50,
        blank=True,
    )
    favorite_tech = models.ForeignKey(
        FavoriteTech,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Favorite Tech'),
    )
    profile_image = CloudinaryField('Profile Image', null=True, blank=True)
    bio = models.TextField(_('Bio'), max_length=500, blank=True)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self) -> str:
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            instance.userprofile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
