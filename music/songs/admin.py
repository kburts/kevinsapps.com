from django.contrib import admin

# Register your models here.
from songs.models import Song, Play

admin.site.register(Song)
admin.site.register(Play)