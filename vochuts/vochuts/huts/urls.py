from django.conf.urls import url

from .views import index, huts_list, huts_detail, booking_pay, booking_thanks

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^huts/$', huts_list, name='list'),
    url(r'^huts/(?P<pk>\d+)/$', huts_detail, name='detail'),
    url(r'^huts/thanks/(?P<uuid_key>[0-9a-z\-]+)/$', booking_thanks, name='thanks'),
    url(r'^booking/(?P<uuid_key>[0-9a-z\-]+)/$', booking_pay, name='pay'),
]
