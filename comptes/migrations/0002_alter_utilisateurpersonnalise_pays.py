# Generated by Django 5.0.4 on 2024-05-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateurpersonnalise',
            name='pays',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
