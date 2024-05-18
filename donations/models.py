from django.db import models
from comptes.models import UtilisateurPersonnalise

# Cette classe du donateur 
class Donateur(UtilisateurPersonnalise):
    nom = models.CharField(max_length=100)
    TYPE_DONATEUR_CHOICES = [
        ('individu', 'Individu'),
        ('entreprise', 'Entreprise'),
        ('organisation', 'Organisation'),
    ]
    type_donateur = models.CharField(max_length=100, choices=TYPE_DONATEUR_CHOICES)
    preferences_besoins = models.CharField(max_length=255)
    statut = models.CharField(max_length=100)
    class Meta:
        abstract = True


#la classe en tant que donateur personne
class DonateurPersonne(Donateur):
    CHOIX_GENRE = [('M', 'Masculin'),('F', 'Féminin'),('Autre', 'Autre')]
    prenom = models.CharField(max_length=50)
    genre = models.CharField(max_length=10, choices=CHOIX_GENRE)
    date_naissance = models.DateField()
    type_donateur = 'Personne'
    class Meta:
        verbose_name = "Donateur Personne"
        verbose_name_plural = "Donateurs Personnes"


#classe du donateur en tant entreprise     
class DonateurEntreprise(Donateur):
    numero_fiscal = models.CharField(max_length=100)
    statut_juridique = models.CharField(max_length=100)
    date_creation = models.DateField()

    class Meta:
        verbose_name = "Donateur Entreprise"
        verbose_name_plural = "Donateurs Entreprise"

        
# classe donateur ent tant que organisation 
class DonateurOrganisation(Donateur):
    numero_fiscal = models.CharField(max_length=100)
    statut_juridique = models.CharField(max_length=100)
    date_creation = models.DateField()

    class Meta:
        verbose_name = "Donateur Organisation"
        verbose_name_plural = "Donateurs Organisation"