from django.contrib import admin

from .models import Hut, Guest, Booking

# Register your models here.
admin.site.register(Hut)
admin.site.register(Guest)
admin.site.register(Booking)