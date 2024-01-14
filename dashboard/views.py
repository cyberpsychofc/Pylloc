from django.shortcuts import render
from users.models import Room

def dashboard(request):
    rooms = list(Room.objects.order_by('num'))
    return render(request,'dashboard.html',{
        'rooms':rooms
    })