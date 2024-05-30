from django.db import models
from comptes.models import UtilisateurPersonnalise
from website_part.models import Besoin
from benevole.models import AgentCollecte
from django.contrib.contenttypes.fields import GenericForeignKey

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
         
class Visiteur(DonateurPersonne):
    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.email})"
    class Meta:
        verbose_name = "Visiteur"
        verbose_name_plural = "Visiteurs"
        db_table = 'visiteur'

#model de la donation 
class Donation(models.Model):
    DONATION_TYPE_CHOICES = [
        ('financier', 'Financier'),
        ('materiel', 'Matériel'),
    ]
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=DONATION_TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    donateur = models.ForeignKey(Donateur, on_delete=models.CASCADE, related_name='donations')
    besoin = models.ForeignKey(Besoin, on_delete=models.CASCADE, related_name='donations')
    def __str__(self):
        return f'Donation {self.id} - {self.type} pour {self.besoin.titre}'
    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donations"
        db_table = 'donation'

class DonationMaterielle(Donation):
    CATEGORIE_CHOICES = [
        ('nourriture', 'Nourriture'),
        ('vetement', 'Vêtement'),
        ('equipement', 'Équipement'),
        ('autre', 'Autre'),
    ]
    description = models.TextField(blank=True, null=True)
    date_reception = models.DateField(blank=True, null=True)
    statut = models.BooleanField(default=False,blank=True,null=True)
    image = models.ImageField(upload_to='donations/', blank=True, null=True)
    categorie = models.CharField(max_length=100, choices=CATEGORIE_CHOICES)
    quantite = models.PositiveIntegerField(default=1)
    agent_collecte = models.ForeignKey(AgentCollecte, on_delete=models.SET_NULL, null=True, blank=True, related_name='donations_materielles')


    class Meta:
        verbose_name = "Donation Matérielle"
        verbose_name_plural = "Donations Matérielles"
        db_table = 'donation_materielle'