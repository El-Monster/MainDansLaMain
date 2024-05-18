from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField

# Définition du gestionnaire de modèle personnalisé pour les utilisateurs
class GestionnaireUtilisateur(BaseUserManager):
    # Méthode pour créer un utilisateur standard
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse e-mail doit être spécifiée")
        email = self.normalize_email(email)
        # Création d'une instance utilisateur avec les champs fournis
        utilisateur = self.model(email=email, **extra_fields)
        # Définition du mot de passe pour l'utilisateur
        utilisateur.set_password(password)
        # Sauvegarde de l'utilisateur dans la base de données
        utilisateur.save(using=self._db)
        return utilisateur

    # Méthode pour créer un superutilisateur
    def create_superuser(self, email, password=None, **extra_fields):
        # Assurer que le superutilisateur a les privilèges appropriés
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Vérification des privilèges du superutilisateur
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Le superutilisateur doit avoir is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Le superutilisateur doit avoir is_superuser=True.")

        # Création de l'utilisateur avec les privilèges de superutilisateur
        return self.create_user(email, password, **extra_fields)

# Définition du modèle utilisateur personnalisé
class UtilisateurPersonnalise(AbstractBaseUser):
    # Champs de l'utilisateur
    nom=models.CharField(max_length=20 ,default='')
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

    # Champs de l'authentification
    est_actif = models.BooleanField(default=True)
    est_personnel = models.BooleanField(default=False)
    est_superutilisateur = models.BooleanField(default=False)

    # Champ requis pour l'authentification
    NOM_UTILISATEUR = 'email'
    # Aucun champ requis supplémentaire lors de la création d'un utilisateur
    USERNAME_FIELD = 'email'

    # Utiliser le gestionnaire de modèle personnalisé
    objets = GestionnaireUtilisateur()

    # Fonction pour obtenir une représentation en chaîne de l'utilisateur
    def __str__(self):
        return self.email

    # class Meta:
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
