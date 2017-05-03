import datetime
from django import forms

from .models import Hut, Booking, Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'email']


class BookingForm(forms.ModelForm):
    date_start = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget)
    date_end = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget)

    class Meta:
        model = Booking
        fields = ['num_guests', 'date_start', 'date_end', 'voc_trip']


class PaymentForm(forms.Form):
    exp_month = forms.IntegerField()
    exp_year = forms.IntegerField()
    number = forms.IntegerField()
    object = 'card'
    cvc = forms.IntegerField()
    name = forms.CharField(label='Full name as appears on card.', max_length=200)
    stripeToken = forms.CharField(max_length=200, required=False)