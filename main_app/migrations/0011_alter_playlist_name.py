# Generated by Django 5.1.1 on 2024-10-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_playlist_color_alter_playlist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
