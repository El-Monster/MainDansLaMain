
from django.db import models

from comptes.models import UtilisateurPersonnalise

# Creation du model benevole   
class Benevole(models.Model):
    prenom = models.CharField(max_length=20, default='')
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), 
    ('F', 'Féminin'), ('Autre', 'Autre')])
    date_naissance = models.DateField()
    statut_disponibilite = models.BooleanField(default=False)
    domaines_de_competences = models.TextField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(UtilisateurPersonnalise, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Bénévole"
        verbose_name_plural = "Bénévoles"
#model pour l'agent de collecte 
class AgentCollecte(UtilisateurPersonnalise):
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    piece_identite = models.FileField(upload_to='pieces_identite/')
    localisation_geographique = models.CharField(max_length=255)
    def __str__(self):
      return f"{self.prenom} - {self.email}"

    class Meta:
        verbose_name = "Agent de Collecte"
        verbose_name_plural = "Agents de Collecte"
        db_table = 'agent_collecte'
#model pour les visiteurs 

