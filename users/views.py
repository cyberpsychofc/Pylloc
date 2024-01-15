from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Room
from .forms import Preference

#allocates room sequentially 
def allocate_seq(request):
    users = User.objects.all().filter(if_allocated=False).order_by('-cgpa')
    rooms = list(Room.objects.filter(user_id__isnull=True).order_by('num'))

    if len(rooms)==0:
        return HttpResponse("No sufficient space available, all rooms reserved.")

    allocation_info = []  # To store information about room allocation
    for user in users:
        room = None #iterable object
        for available_room in rooms:
            if available_room.year == user.year and available_room.user_id is None and not user.if_allocated:
                room = available_room
                room.user = user
                user.if_allocated = True
                room.save()  # Save changes to the Room instance
                user.save()  # Save changes to the User instance


                allocation_info.append(f"Student {user.name} (CGPA: {user.cgpa}) allocated to Room {room.num}")
                break

        if room is not None:
            rooms.remove(room)

    if len(allocation_info) == 0:
        return HttpResponse("No sufficient space available")
    else:
        return HttpResponse('\n'.join(allocation_info),content_type="text/plain")

#allocate-as-per-choice
def allocate_apc(request):
    users = User.objects.all().filter(if_allocated=False).order_by('-cgpa')
    rooms = list(Room.objects.filter(user_id__isnull=True).order_by('num'))

    if len(rooms)==0:
        return HttpResponse("No sufficient space available, all rooms reserved.")
    
    allocation_info = []  # To store information about room allocation

    for user in users:
        room = None #iterable object
        for available_room in rooms:
            if available_room.num == user.room1 and available_room.user_id is not None:
                continue
            if available_room.num == user.room2 and available_room.user_id is not None:
                continue
            if available_room.num == user.room3 and available_room.user_id is not None:
                continue
            
            if available_room.year == user.year and not user.if_allocated:
                room = available_room
                room.user = user
                user.if_allocated = True
                room.save()  # Save changes to the Room instance
                user.save()  # Save changes to the User instance


                allocation_info.append(f"Student {user.name} (CGPA: {user.cgpa}) allocated to Room {room.num}")
                break
        if room is not None:
            rooms.remove(room)

    if len(allocation_info) == 0:
        return HttpResponse("No sufficient space available")
    else:
        return HttpResponse('\n'.join(allocation_info),content_type="text/plain")
    
#take preference from the user
def preference(request, user_pk):
    user = get_object_or_404(User,pk=user_pk)
    rooms = list(Room.objects.filter(user_id__isnull=True).order_by('num'))

    if (request.method == 'POST'):
        form = Preference(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = Preference()

    return render(request,'preference.html',{
        #variable-mapping
        'form':form,
        'rooms':rooms
    })