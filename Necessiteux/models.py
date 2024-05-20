from django.db import models
from comptes.models import UtilisateurPersonnalise
# Creation de la classe Necessiteux
class Necessiteux(models.Model):
    TYPE_CHOICES = [('personne', 'Personne'),('organisation', 'Organisation')]
    #nom = models.CharField(max_length=100)
    type_necessiteux = models.CharField(max_length=100,choices=TYPE_CHOICES)
    user = models.ForeignKey(UtilisateurPersonnalise, on_delete=models.CASCADE)
    class Meta:
        abstract=True
        
#creation de la classe Necessiteux en tant que personne
class NecessiteuxPersonne(Necessiteux):
    choix_genre=[('M', 'Masculin'), ('F', 'Féminin'), ('Autre', 'Autre')]
    prenom = models.CharField(max_length=20)
    genre = models.CharField(max_length=10, choices=choix_genre)
    date_naissance = models.DateTimeField()
    class Meta:
        verbose_name = "Nécessiteux Personne"
        verbose_name_plural = "Nécessiteux Personnes"
      
#creation de la classe Necessiteux ent tant que Organisation 
class NecessiteuxOrganisation(Necessiteux):
    choix_statut=[('EI', 'Entreprise Individuelle'),
                  ('EIRL', 'Entreprise Individuelle a Responsabilité Limitée'),
                  ('SARL', 'Societé à Responsabilité Limitée'),
                  ('EURL', ' Entreprise Unipersonnelle à Responsabilité Limitée'),
                  ('EURL', 'Société par Actions Simplifiée'),
                  ('SA', 'Société Anonyme'),
                  
                  ]
    numero_matd = models.CharField(unique=True ,max_length=100)
    agrement_maspfe = models.CharField(unique=True, max_length=100)
    statut_juridique = models.CharField(max_length=100,choices=choix_statut)
    date_creation = models.DateTimeField()
    class Meta:
        verbose_name = "Nécessiteux Organisation"
        verbose_name_plural = "Nécessiteux Organisations"