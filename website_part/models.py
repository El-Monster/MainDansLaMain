from django.db import models

# La classe du formulaire de contact
class Message(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
