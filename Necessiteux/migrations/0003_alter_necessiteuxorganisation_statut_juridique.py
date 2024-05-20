# Generated by Django 5.0.3 on 2024-05-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Necessiteux', '0002_remove_necessiteuxorganisation_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='necessiteuxorganisation',
            name='statut_juridique',
            field=models.CharField(choices=[('EI', 'Entreprise Individuelle'), ('EIRL', 'Entreprise Individuelle a Responsabilité Limitée'), ('SARL', 'Societé A responsabilité Limitée')], max_length=100),
        ),
    ]
