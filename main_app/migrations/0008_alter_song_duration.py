# Generated by Django 5.1.1 on 2024-10-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_playlist_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DurationField(max_length=10, verbose_name='Song Duration'),
        ),
    ]
