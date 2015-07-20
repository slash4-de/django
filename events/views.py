from django.shortcuts import render

from .models import Event

def home(request):
    return render(request, 'events/home.html')

def list(request):
   event_list = Event.objects.all();
   return render(request, 'events/list.html', {'event_list': event_list})

def detail(request, id):
   event = Event.objects.get(id=id)
   return render(request, 'events/detail.html', {'event': event})