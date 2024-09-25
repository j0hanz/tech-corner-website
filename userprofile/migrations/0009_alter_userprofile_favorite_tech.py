# Generated by Django 4.2.9 on 2024-09-25 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_alter_userprofile_favorite_tech_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.favoritetech', verbose_name='Favorite Tech'),
        ),
    ]
