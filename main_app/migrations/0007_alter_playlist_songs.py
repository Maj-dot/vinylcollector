# Generated by Django 5.1.1 on 2024-10-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_playlist_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(related_name='playlists', to='main_app.song'),
        ),
    ]
