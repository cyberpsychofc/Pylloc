from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    cgpa = models.IntegerField()
    mob = models.CharField(max_length=10)
    email = models.CharField(max_length=90)
    if_allocated = models.BooleanField(default=False)
    #room-preferences
    room1 = models.IntegerField(null=True)
    room2 = models.IntegerField(null=True)
    room3 = models.IntegerField(null=True)

class Room(models.Model):
    num = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    # to_field, to change reference of foreign key
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 

# class postalloc(models.Model):
    # Room.num = models.ForeignKey()
    # User.id = models.ForeignKey()
