# Generated by Django 5.0 on 2024-01-09 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_room_if_allocated_room_student_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='student_id',
            new_name='student',
        ),
    ]
