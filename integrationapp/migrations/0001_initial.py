# Generated by Django 3.2 on 2022-01-23 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='trello workspace url')),
                ('project', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trello', to='automation.project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'Trello',
                'verbose_name_plural': 'Trelloes',
            },
        ),
        migrations.CreateModel(
            name='Discord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='discord server url')),
                ('project', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discord', to='automation.project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'Discord',
                'verbose_name_plural': 'Discords',
            },
        ),
    ]
