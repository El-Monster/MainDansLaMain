from django.db import models
from Necessiteux.models import Necessiteux

class Besoin(models.Model):
    URGENCE_CHOICES = [
        ('Faible', 'Faible'),
        ('Moyen', 'Moyen'),
        ('Élevé', 'Élevé'),
    ]
    STATUT_CHOICES = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé'),
    ]
    necessiteux = models.ForeignKey(Necessiteux, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    degre_urgence = models.CharField(max_length=20, choices=URGENCE_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_limite = models.DateTimeField(blank=True,null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='En attente')
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='besoins/images/', blank=True, null=True)
    document = models.FileField(upload_to='besoins/documents/', blank=True, null=True)
    video = models.FileField(upload_to='besoins/videos/', blank=True, null=True)
    def __str__(self):
        return self.titre

    class Meta:
        db_table = 'besoin'
        ordering = ['date_creation']
        verbose_name = 'Besoin'
        verbose_name_plural = 'Besoins '
        
class BesoinMateriel(Besoin):
    CATEGORIE_CHOICES = [
        ('Nourriture', 'Nourriture'),
        ('Vêtements', 'Vêtements'),
        ('Logement', 'Logement'),
        ('Éducation', 'Éducation'),
    ]
    
    categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES)
    quantite = models.IntegerField()
    class Meta:
        db_table = 'besoin_materiel'
        verbose_name = "Besoin Matériel"
        verbose_name_plural = "Besoins Matériels"

class BesoinFinancier(Besoin):
    montant_souhaite = models.DecimalField(max_digits=10, decimal_places=2)
    montant_collecte = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,blank=True,null=True)

    class Meta:
        db_table = 'besoin_financier'
        verbose_name = "Besoin Financier"
        verbose_name_plural = "Besoins Financiers"
# le model pour le besoin en benevole
class BesoinDeBenevoles(Besoin):
    duree = models.CharField(max_length=100)  # Par exemple, '2 semaines'
    nombre_de_benevoles = models.PositiveIntegerField()
    competences_demandees = models.TextField()  # Par exemple, 'Compétences en gestion de projet, communication'

    class Meta:
        db_table = 'besoin_de_benevoles'
        verbose_name = 'Besoin de bénévoles'
        verbose_name_plural = 'Besoins de bénévoles'

    def __str__(self):
        return f"{self.titre} - Besoin de bénévoles"