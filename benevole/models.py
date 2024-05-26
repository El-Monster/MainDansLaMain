
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
