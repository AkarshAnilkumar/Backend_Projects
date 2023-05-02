from django.shortcuts import render
# from django.http import HttpResponse
from .models import hotelroom

roomsold = [
    {"id": 1, "name": "Lets learn"},
    {"id": 2, "name": "Python from"},
    {"id": 3, "name": "basics"},
]
roomdict = {'ok': roomsold}


def home(request):
    rooms = hotelroom.objects.all()
    context = {'room': rooms}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html', roomdict)


def room2(request):
    return render(request, 'room2.html', roomdict)


def room3(request):
    return render(request, 'room3.html', roomdict)
