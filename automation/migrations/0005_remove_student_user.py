# Generated by Django 3.2 on 2022-01-22 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_command_meeting_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]