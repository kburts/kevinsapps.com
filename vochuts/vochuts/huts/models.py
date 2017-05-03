import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.datetime_safe import date


class Hut(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2, help_text='Price as decimal number, eg. 19.23')
    capacity = models.PositiveIntegerField(help_text='Recommended capacity.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])


class Guest(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Booking(models.Model):
    hut = models.ForeignKey(Hut)
    guest = models.ForeignKey(Guest)
    num_guests = models.IntegerField(default=1)
    date_start = models.DateField()
    date_end = models.DateField()
    voc_trip = models.BooleanField(default=False, help_text='VOC trips are free.')
    paid = models.BooleanField(default=False)
    uuid_key = models.UUIDField(default=uuid.uuid4, editable=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def duration(self):
        return (self.date_end - self.date_start).days

    @property
    def total_cost(self):
        return self.duration * self.hut.price * self.num_guests

    @property
    def total_cost_cents(self):
        return int(self.total_cost * 100)

    @property
    def booking_status(self):
        return 'Paid' if self.paid else 'Not paid'

    @property
    def past_booking(self):
        return self.date_end < date.today()

    def save(self, *args, **kwargs):
        if self.date_end < self.date_start:
            raise ValidationError('Beep Boop.. Cannot have a negative length stay')
        if self.date_start < date.today():
            raise ValidationError('Beepidy boop.. Cannot create booking in the past.')
        super(Booking, self).save(*args, **kwargs)

    def send_booking_email(self):
        manage_url = '{}{}'.format(settings.URL_BASE, reverse('thanks', args=[str(self.uuid_key)]))
        body = """
        Thanks for letting us know you want to stay in one of the huts!
        This is the info we have for your booking:
            Date: {date_start} - {date_end}
            Hut: {hut_name}
            Guests: {num_guests}
        Use this link to manage your booking and pay: {manage_url}
        """.format(date_start=self.date_start, date_end=self.date_end, hut_name=self.hut.name, num_guests=self.num_guests, manage_url=manage_url)
        subject = 'Manage Your VOC Hut Booking'
        to = self.guest.email
        send_mail(subject=subject, message=body, from_email='VOC Huts <huts@kevinsapps.com>', recipient_list=[to])

    def __str__(self):
        return '{} - {}. {} {}'.format(self.date_start, self.date_end, self.hut, self.guest)


class Payment(models.Model):
    booking = models.ForeignKey(Booking)
    amount = models.DecimalField(max_digits=4, decimal_places=2, help_text='Price as decimal number, eg. 19.23')
    paid = models.BooleanField(default=False)
