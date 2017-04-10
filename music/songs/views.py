from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from songs.models import Song, Play

User = get_user_model()


@login_required(login_url='/log_in/')
def user_list(request):
    """
    NOTE: This is fine for demonstration purposes, but this should be
    refactored before we deploy this app to production.
    Imagine how 100,000 users logging in and out of our app would affect
    the performance of this code!
    """
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'songs/user_list.html', {'users': users})


def home(request):
    """
    Homepage view. Listens for new plays
    """
    plays = Play.objects.order_by('-created')[:10]
    return render(request, 'songs/home.html', {'plays': plays})


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('songs:user_list'))
        else:
            print(form.errors)
    return render(request, 'songs/log_in.html', {'form': form})


@login_required(login_url='/log_in/')
def log_out(request):
    logout(request)
    return redirect(reverse('songs:log_in'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('songs:log_in'))
        else:
            print(form.errors)
    return render(request, 'songs/sign_up.html', {'form': form})


@csrf_exempt
def scrobble(request):
    print('Got Scrobble Request!!!')
    print(vars(request))

    response_status = 'OK'
    session_token = 'dc8fcc9d4d019427a506c438e1f48b55'
    now_playing = ''.join(['http://', str(get_current_site(request)), '/scrobble/np'])
    submit = ''.join(['http://', str(get_current_site(request)), '/scrobble/submit'])

    response = "{}\n{}\n{}\n{}\n".format(response_status, session_token, now_playing, submit)
    #response = "OK\ndc8fcc9d4d019427a506c438e1f48b55\nhttp://192.168.99.100:5000/\nhttp://192.168.99.100:5000\n"
    return HttpResponse(response, content_type='application/octet-stream')


@csrf_exempt
def now_playing(request):
    if request.method == 'POST':
        session = request.POST.get('s', '')  # not used @TODO set this up some time
        artist = request.POST.get('a', '')
        track = request.POST.get('t', '')
        album = request.POST.get('b', '')
        length = request.POST.get('l', '') or None  # Set to None instead of '' to make django happy.
        track_number = request.POST.get('n', '') or None

        song = Song.objects.get_or_create(artist=artist, title=track, album=album, length=length, track_number=track_number)
        play = Play.objects.create(song=song[0])  # @TODO user=me

    return HttpResponse('OK\n')

@csrf_exempt
def submit_track(request):
    # @TODO: TO implement
    return HttpResponse('OK\n')

@csrf_exempt
def ok_200(request):
    print('200 OK!!!')
    print(request.META)
    print(vars(request))
    print('POST')
    print(request.POST)

    response_text = "OK\n"
    response = HttpResponse(response_text)
    #response['Connection'] = 'keep-alive'
    #response['Content-Type'] = 'application/octet-stream'
    #response['Content-Length'] = '15'
    #response['Date'] = 'Sat, 04 Mar 2017 21:04:21 GMT'
    #response['Server'] = 'openresty/1.9.7.3'
    #response['Transfer-Encoding'] = 'chunked'

    return response