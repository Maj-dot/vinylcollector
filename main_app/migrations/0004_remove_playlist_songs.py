# Generated by Django 5.1.1 on 2024-10-05 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_playlist_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='songs',
        ),
    ]
