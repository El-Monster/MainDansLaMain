from django.db import models

from comptes.models import UtilisateurPersonnalise

# Create your models here.
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
