# Generated by Django 4.2.9 on 2024-05-26 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]