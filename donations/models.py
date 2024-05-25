from django.db import models
from comptes.models import UtilisateurPersonnalise

class Donateur(UtilisateurPersonnalise):
    TYPE_DONATEUR_CHOICES = [
        ('individu', 'Individu'),
        ('entreprise', 'Entreprise'),
        ('organisation', 'Organisation'),
    ]
    type_donateur = models.CharField(max_length=100, choices=TYPE_DONATEUR_CHOICES)
    preferences_besoins = models.CharField(max_length=255, blank=True, null=True)
    statut_donateur = models.CharField(max_length=100, blank=True, null=True)  # Renommage du champ pour éviter le conflit

    class Meta:
        db_table = 'donateur'
        verbose_name = "Donateur"
        verbose_name_plural = "Donateurs"


class DonateurPersonne(Donateur):
    CHOIX_GENRE = [('M', 'Masculin'),('F', 'Féminin'),('Autre', 'Autre')]
    prenom = models.CharField(max_length=50)
    genre = models.CharField(max_length=10, choices=CHOIX_GENRE)
    date_naissance = models.DateField()

    class Meta:
        db_table = 'donateur_personne'
        verbose_name = "Donateur Personne"
        verbose_name_plural = "Donateurs Personnes"

class DonateurEntreprise(Donateur):
    numero_fiscal = models.CharField(max_length=100)
    statut_juridique = models.CharField(max_length=100)
    date_creation = models.DateField()

    class Meta:
        db_table = 'donateur_entreprise'
        verbose_name = "Donateur Entreprise"
        verbose_name_plural = "Donateurs Entreprises"

class DonateurOrganisation(Donateur):
    numero_MATD = models.CharField(max_length=100)
    statut_juridique = models.CharField(max_length=100)
    date_creation = models.DateField()

    class Meta:
        db_table = 'donateur_organisation'
        verbose_name = "Donateur Organisation"
        verbose_name_plural = "Donateurs Organisations"
