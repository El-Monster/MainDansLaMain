# Generated by Django 5.0.3 on 2024-05-20 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Necessiteux', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='necessiteuxorganisation',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='necessiteuxpersonne',
            name='nom',
        ),
    ]
