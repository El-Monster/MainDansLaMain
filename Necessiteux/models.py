from django.db import models
from comptes.models import UtilisateurPersonnalise
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
"""@receiver(post_save, sender=UtilisateurPersonnalise)
def create_necessiteux(sender, instance, created, **kwargs):
    if created:
        Necessiteux.objects.create(user=instance)

@receiver(post_save, sender=UtilisateurPersonnalise)
def save_necessiteux(sender, instance, **kwargs):
    instance.necessiteux.save()"""
    

from django.db import models
from comptes.models import UtilisateurPersonnalise

class Necessiteux(UtilisateurPersonnalise):
    TYPE_CHOICES = [('personne', 'Personne'), ('organisation', 'Organisation')]
    #user = models.OneToOneField(UtilisateurPersonnalise, on_delete=models.CASCADE, primary_key=True)
    type_necessiteux = models.CharField(max_length=100, choices=TYPE_CHOICES)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Nécessiteux"
        verbose_name_plural = "Nécessiteux"
        db_table = "necessiteux"

class NecessiteuxPersonne(Necessiteux):
    
    choix_genre = [('M', 'Masculin'), ('F', 'Féminin'), ('Autre', 'Autre')]
    prenom = models.CharField(max_length=20)
    genre = models.CharField(max_length=10, choices=choix_genre)
    date_naissance = models.DateTimeField()

    class Meta:
        verbose_name = "Nécessiteux Personne"
        verbose_name_plural = "Nécessiteux Personnes"
        db_table = "necessiteux_personne"

class NecessiteuxOrganisation(Necessiteux):
    choix_statut = [
        ('EI', 'Entreprise Individuelle'),
        ('EIRL', 'Entreprise Individuelle a Responsabilité Limitée'),
        ('SARL', 'Societé à Responsabilité Limitée'),
        ('EURL', ' Entreprise Unipersonnelle à Responsabilité Limitée'),
        ('EURL', 'Société par Actions Simplifiée'),
        ('SA', 'Société Anonyme'),
    ]
    numero_matd = models.CharField(unique=True, max_length=100)
    agrement_maspfe = models.CharField(unique=True, max_length=100)
    statut_juridique = models.CharField(max_length=100, choices=choix_statut)
    date_creation = models.DateTimeField()

    class Meta:
        verbose_name = "Nécessiteux Organisation"
        verbose_name_plural = "Nécessiteux Organisations"
        db_table = "necessiteux_organisation"
