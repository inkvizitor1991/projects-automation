# Generated by Django 3.2 on 2022-01-23 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrationapp', '0005_alter_trelloboard_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trelloboard',
            old_name='project_command',
            new_name='command',
        ),
    ]
