# Generated by Django 5.0 on 2024-01-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_student_room_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='room1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='room2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='room3',
            field=models.IntegerField(null=True),
        ),
    ]
