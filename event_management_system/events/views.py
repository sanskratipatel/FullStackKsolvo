from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserSignupForm, EventForm
from .models import Event, Notification
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Notification
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# User Login
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('event_list')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# User Signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a page after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
# Event List
@login_required
def list_events(request):
    events = Event.objects.all()
    return render(request, 'events/list_events.html', {'events': events})

# Event Detail
@login_required
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event_detail.html', {'event': event})

# Event Creation
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            # Create a notification for attendees
            Notification.objects.create(user=request.user, message="Event created", event=event)
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

# Notification List
# @login_required
# def notification_list(request):
#     notifications = Notification.objects.filter(user=request.user, is_read=False)
#     return render(request, 'notification.html', {'notifications': notifications})
@login_required

def view_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications.html', {'notifications': notifications})