from  datetime import datetime
from django.shortcuts import render

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