import json
from channels import Group
from django.contrib.auth import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LoggedInUser, Play


@receiver(user_logged_in)
def on_user_login(sender, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))


@receiver(user_logged_out)
def on_user_logout(sender, **kwargs):
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()


@receiver(post_save, sender=Play)
def on_play(sender, instance, **kwargs):
    song = instance.song.get_song_as_dict()
    song.update({'time': str(instance.created)})
    Group('music').send({
        'text': json.dumps(song)
    })
    print('send message to group all')
