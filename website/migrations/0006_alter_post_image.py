# Generated by Django 4.2.9 on 2024-09-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
