# Generated by Django 5.1.1 on 2024-10-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_playlist_description_playlist_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
