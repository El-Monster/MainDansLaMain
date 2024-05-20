# Generated by Django 5.0.3 on 2024-05-20 12:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benevole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(default='', max_length=20)),
                ('genre', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin'), ('Autre', 'Autre')], max_length=10)),
                ('date_naissance', models.DateField()),
                ('statut_disponibilite', models.BooleanField(default=False)),
                ('domaines_de_competences', models.TextField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bénévole',
                'verbose_name_plural': 'Bénévoles',
            },
        ),
    ]
