import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.datetime_safe import date
from django.views.decorators.csrf import csrf_exempt

from huts.forms import GuestForm, BookingForm, PaymentForm
from huts.models import Hut, Booking, Guest


def index(request):
    huts = Hut.objects.all()

    context = {
        'huts': huts
    }

    return render(request, 'huts/home.html', context=context)


def huts_list(request):
    return index(request)


def huts_detail(request, pk):
    hut = Hut.objects.get(pk=pk)
    bookings = Booking.objects.filter(hut=hut, date_end__gte=date.today()).order_by('date_start')

    if request.method == 'POST':
        guest_form = GuestForm(request.POST)
        booking_form = BookingForm(request.POST)

        if guest_form.is_valid():
            guest, created = Guest.objects.get_or_create(**guest_form.cleaned_data)

            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.guest = guest
                booking.hut = Hut.objects.get(pk=pk)
                booking.save()

                booking.send_booking_email()

                return redirect('thanks', str(booking.uuid_key))

    else:
        guest_form = GuestForm()
        booking_form = BookingForm()

    context = {
        'hut': hut,
        'bookings': bookings,
        'guest_form': guest_form,
        'booking_form': booking_form
    }

    return render(request, 'huts/hut_detail.html', context=context)


def booking_thanks(request, uuid_key):
    manage_url = request.build_absolute_uri(reverse('pay', args=[uuid_key]))

    return render(request, 'huts/booking_thanks.html', {'key': uuid_key, 'manage_url': manage_url})


@csrf_exempt
def process_payment(request, token):
    pass


def booking_pay(request, uuid_key):
    booking = Booking.objects.get(uuid_key=uuid_key)

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            charge = {
                'amount': booking.total_cost_cents,
                'currency': 'cad',
                'source': {
                    'exp_month': form.cleaned_data['exp_month'],
                    'exp_year': form.cleaned_data['exp_year'],
                    'number': form.cleaned_data['number'],
                    'object': 'card',
                    'cvc': form.cleaned_data['cvc']
                }
            }
            print(form)
            stripe.api_key = settings.STRIPE_SECRET_KEY
            response = stripe.Charge.create(**charge)
            print(response)

            booking.paid = True
            booking.save()

            return redirect('pay', booking.uuid_key)

    else:
        form = PaymentForm()

    return render(request, 'huts/booking_pay.html', {'form': form, 'booking': booking})


