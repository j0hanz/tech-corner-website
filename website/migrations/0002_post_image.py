# Generated by Django 4.2.9 on 2024-09-24 22:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
