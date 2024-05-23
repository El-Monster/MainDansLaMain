from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

class GestionnaireUtilisateur(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("L'adresse e-mail doit être spécifiée"))
        email = self.normalize_email(email)
        utilisateur = self.model(email=email, **extra_fields)
        utilisateur.set_password(password)
        utilisateur.save(using=self._db)
        return utilisateur

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Le superutilisateur doit avoir is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Le superutilisateur doit avoir is_superuser=True."))

        return self.create_user(email, password, **extra_fields)

class UtilisateurPersonnalise(AbstractBaseUser, PermissionsMixin):
    nom = models.CharField(max_length=20, default='')
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    pays = CountryField(blank_label="Votre pays", blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    statut = models.CharField(max_length=100, blank=True, null=True)
    statut_verification = models.BooleanField(default=False)
    date_creation_compte = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    bibliographie = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_superuser = models.BooleanField(_('superuser status'), default=False,
                                   help_text=_('Designates that this user has all permissions without explicitly assigning them.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = GestionnaireUtilisateur()

    def __str__(self):
        return self.email


    #     abstract = True  # Définit cette classe comme une classe abstraite

# Définition du modèle d'administrateur
class Administrateur(models.Model):
    prenom=models.CharField(max_length=20 ,default='')
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin'), ('Autre', 'Autre')], blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    role_administratif = models.CharField(max_length=100)
    date_debut_administration = models.DateField()
    user = models.ForeignKey(UtilisateurPersonnalise, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Administrateur"
        verbose_name_plural = "Administrateurs"
        
# class Benevole(UtilisateurPersonnalise):
#     prenom = models.CharField(max_length=20, default='')
#     genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin'), ('Autre', 'Autre')], blank=True, null=True)
#     date_naissance = models.DateField(blank=True, null=True)
#     statut_disponibilite = models.BooleanField(default=False)
#     domaines_de_competences = models.TextField(max_length=255, blank=True, null=True)

#     class Meta:
#         verbose_name = "Bénévole"
#         verbose_name_plural = "Bénévoles"
