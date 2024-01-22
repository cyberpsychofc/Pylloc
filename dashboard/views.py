from django.shortcuts import render
from users.models import Room
from .forms import SignUpForm, AddRoom

def dashboard(request):
    rooms = list(Room.objects.order_by('num'))
    room_mat = []

    for i in range(0,len(rooms),4):
        room_mat.append(rooms[i:i+4])
    return render(request,'dashboard.html',{
        'rooms':rooms,
        'room_mat':room_mat,
    })

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request,'signup.html',{
        'form':form
    })

def rms_dash(request):
    if request.method == 'POST':
        form = AddRoom(request.POST)
        '''if form.is_valid():
            form.save()'''
    else:
        form = AddRoom()
    return render(request,'rms.html',{
        'form':form
    })