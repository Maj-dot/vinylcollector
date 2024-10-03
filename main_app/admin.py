from django.contrib import admin
from .models import Vinyl, Song, Playlist
# Register your models here.
admin.site.register(Vinyl)
admin.site.register(Song)
admin.site.register(Playlist)