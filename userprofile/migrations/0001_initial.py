# Generated by Django 4.2.9 on 2024-05-26 10:34

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PC', 'PC'), ('Mobile', 'Mobile'), ('Tablet', 'Tablet'), ('AI', 'AI'), ('Raspberry Pi', 'Raspberry Pi'), ('Networking', 'Networking'), ('Other', 'Other'), ('Laptop', 'Laptop'), ('Smartphone', 'Smartphone'), ('Desktop', 'Desktop'), ('Smart Home', 'Smart Home'), ('Wearable', 'Wearable'), ('Gaming Console', 'Gaming Console'), ('VR', 'VR'), ('Drone', 'Drone'), ('IoT', 'IoT'), ('Cloud Computing', 'Cloud Computing'), ('Cyber Security', 'Cyber Security')], max_length=50, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Favorite Tech',
                'verbose_name_plural': 'Favorite Technologies',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(blank=True, max_length=300, null=True, unique=True, verbose_name='Email Address')),
                ('profile_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Profile Image')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='Bio')),
                ('favorite_tech', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.favoritetech', verbose_name='Favorite Tech')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
