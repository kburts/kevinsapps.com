from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from songs.views import user_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('songs.urls', namespace='songs')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]