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
    return render(request, 'events/detail.html', {'event': event})

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
    return render(request, 'events/detail.html', {'event': event, 'message': message})
