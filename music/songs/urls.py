from django.conf.urls import url
from .views import log_in, log_out, sign_up, user_list, scrobble, ok_200, now_playing

urlpatterns = [
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^log_out/$', log_out, name='log_out'),
    url(r'^sign_up/$', sign_up, name='sign_up'),
    url(r'^scrobble/$', scrobble, name='scrobble'),
    url(r'^scrobble/np$', now_playing, name='scrobble_now_playing'),
    url(r'^scrobble/submit', ok_200, name='scrobble_submit_track'),
    url(r'^$', user_list, name='user_list'),
]