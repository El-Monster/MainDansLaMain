# Generated by Django 5.0.3 on 2024-05-18 15:05

import django.db.models.deletion
import django.db.models.manager
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UtilisateurPersonnalise',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nom', models.CharField(default='', max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('pays', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('ville', models.CharField(blank=True, max_length=100, null=True)),
                ('statut', models.CharField(blank=True, max_length=100, null=True)),
                ('statut_verification', models.BooleanField(default=False)),
                ('date_creation_compte', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('bibliographie', models.TextField(blank=True, null=True)),
                ('est_actif', models.BooleanField(default=True)),
                ('est_personnel', models.BooleanField(default=False)),
                ('est_superutilisateur', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objets', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(default='', max_length=20)),
                ('genre', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Féminin'), ('Autre', 'Autre')], max_length=10, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('role_administratif', models.CharField(max_length=100)),
                ('date_debut_administration', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comptes.utilisateurpersonnalise')),
            ],
            options={
                'verbose_name': 'Administrateur',
                'verbose_name_plural': 'Administrateurs',
            },
        ),
    ]
