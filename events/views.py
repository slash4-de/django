from  datetime import datetime
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Event

def home(request):
    try:
        event = Event.objects.filter(date__gt=datetime.now()).order_by('date')[:1][0]
    except:
        event = []
    return render(request, 'events/home.html', {'event': event})

def list(request):
    event_list = Event.objects.all().order_by('date');
    return render(request, 'events/list.html', {'event_list': event_list})

def detail(request, id):
   event = Event.objects.get(id=id)
   joined = event.guest.filter(id=request.user.id)
   return render(request, 'events/detail.html', {'event': event, 'joined': joined})

def register(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           new_user = form.save()
           return HttpResponseRedirect("/")
    else:
       form = UserCreationForm()
    return render(request, "users/register.html", {
       'form': form,
    })

@login_required
def join(request, event_id):
    try:
        # already joined
        event = Event.objects.get(id=event_id, guest=request.user)
        message = "You have already joined this event"
    except Event.DoesNotExist as e:
        # Event exist but joined
        try:
            event = Event.objects.get(id=event_id)
            event.guest.add(request.user)
            event.save()
            message = "You have joined this event"
        except Event.DoesNotExist as e:
            message = "Error on event joining"

    event = Event.objects.get(id=event_id)
    joined = event.guest.filter(id=request.user.id)
    return render(request, 'events/detail.html', {
        'event': event,
        'message': message,
        'joined': joined
    })

@login_required
def cancel(request, event_id):
    try:
        event = Event.objects.get(id=event_id, guest=request.user)
        event.guest.remove(request.user)
        event.save()
        message = "Your request not to attend has been saved"
    except Event.DoesNotExist as e:
            message = "Error on cancelling your attedance on event"

    event = Event.objects.get(id=event_id)
    joined = event.guest.filter(id=request.user.id)
    return render(request, 'events/detail.html', {
        'event': event,
        'message': message,
        'joined': joined
    })
