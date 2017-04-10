from django.conf import settings
from django.db import models

# Create your models here.


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user')


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, blank=True)
    album = models.CharField(max_length=200, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True)
    track_number = models.PositiveIntegerField(null=True, blank=True)

    year = models.PositiveIntegerField(null=True)

    def __str__(self):
        return '{} - {}'.format(self.artist, self.title)

    def get_song_as_dict(self):
        return {
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            #'year': self.year,
        }


class Play(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    song = models.ForeignKey(Song, related_name='play')

    def __str__(self):
        return '{} - {}'.format(self.song.artist, self.song.title)
