from django.shortcuts import render
from users.models import Room

def dashboard(request):
    rooms = list(Room.objects.order_by('num'))
    room_mat = []

    for i in range(0,len(rooms),4):
        room_mat.append(rooms[i:i+4])
    return render(request,'dashboard.html',{
        'rooms':rooms,
        'room_mat':room_mat,
    })