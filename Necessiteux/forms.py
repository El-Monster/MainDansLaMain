from django import forms
from .models import NecessiteuxPersonne, NecessiteuxOrganisation
from .models import BesoinMateriel, BesoinFinancier,BesoinDeBenevoles


# Formulaire de création de compte de type "nécéssiteux personne"
class NecessiteuxPersonneForm(forms.ModelForm):
     password_confirmation = forms.CharField(
     widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
     label='Confirmer le mot de passe'
     )
     class Meta:
        model = NecessiteuxPersonne
        
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
            'genre': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control  form-control-lg'}),
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'tel'}),
            'pays': forms.Select(attrs={'class': 'form-select form-select-lg pays', 'id': 'pays', 'onchange': 'chargerVilles()'}),
            'ville': forms.Select(attrs={'class': 'form-select form-select-lg villes', 'id': 'villes'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'password_confirmation': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }

        labels = {
            'prenom': 'Prénom',
            'nom':'Nom',
            'genre': 'Genre',
            'date_naissance': 'Date de naissance',
            'email': 'Adresse e-mail',
            'telephone': 'Téléphone',
            'pays': 'Votre pays d\'origine',
            'ville': 'Votre ville d\'origine',
            'photo': 'Choisissez votre photo de profil',
            'password': 'Mot de passe'
        }
        
        fields = [
            'prenom',
            'genre',
            'date_naissance',
            'email', 
            'telephone', 
            'pays',
            'ville', 
            'photo',
            'nom',
            'password'
        ]
        
        from django import forms


# Formulaire de création de compte de type "nécéssiteux organisation"
class NecessiteuxOrganisationForm(forms.ModelForm):
    password_confirmation = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
    label='Confirmer le mot de passe'
    )
    
    class Meta:
        model = NecessiteuxOrganisation
        fields = [
            'numero_matd',
            'agrement_maspfe',
            'statut_juridique',
            'date_creation',
            'email', 
            'telephone', 
            'pays', 
            'ville', 
            'photo',
            'nom',
            'password'
        ]

        widgets = {
            'numero_matd': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'statut_juridique': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg'}),
            'agrement_maspfe': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control form-control-lg'}),
            'telephone': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control form-control-lg'}),
            'pays': forms.Select(attrs={'class': 'form-select form-select-lg pays', 'id': 'pays', 'onchange': 'chargerVilles()'}),
            'ville': forms.Select(attrs={'class': 'form-select form-select-lg villes', 'id': 'villes'}),
            'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control form-control-lg'}),
            'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'password_confirmation': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control form-control-lg'})
        }
          
        labels = {
            'numero_matd': 'Numéro MATD',
            'agrement_maspfe': 'Agrément MASFE',
            'statut_juridique': 'Statut juridique',
            'date_creation': 'Date de création', 
            'email': 'Adresse e-mail',
            'telephone': 'Téléphone',
            'pays': 'Pays',
            'ville': 'Ville',
            'photo': 'Photo de profil',
            'nom':"Nom",
            'password':"Mot de passe"
        }


# Formulaire d'envoi de "besoin matériel"
class BesoinMaterielForm(forms.ModelForm):
    class Meta:
        model = BesoinMateriel
        fields = [
            'titre',
            'description',
            'degre_urgence',
            'image',
            'document',
            'video',
            'categorie',
            'quantite',
        ]

        labels = {
            'titre': 'Titre du besoin',
            'description': 'Description du besoin',
            'categorie': 'Catégorie',
            'quantite': 'Quantité',
            'degre_urgence': 'Degré d\'urgence',
            'image': 'Image associée',
            'document': 'Document associé',
            'video': 'Vidéo associée',
        }

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': '4'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'min': '1'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'document': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'video': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'categorie': forms.Select(attrs={'class': 'form-select form-select-lg'}),
        }


# Formulaire d'envoi de "besoin financier"
class BesoinFinancierForm(forms.ModelForm):
    class Meta:
        model = BesoinFinancier
        
        fields = [
            'titre',
            'description',
            'degre_urgence',
            'image',
            'document',
            'video',
            'montant_souhaite',
        ]

        labels = {
            'titre': 'Titre du besoin',
            'description': 'Description du besoin',
            'degre_urgence': 'Degré d\'urgence',
            'montant_souhaite': 'Montant Nécessaire',
            'image': 'Image associée',
            'document': 'Document associé',
            'video': 'Vidéo associée',
        }

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': '4'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'document': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'video': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'montant_souhaite': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }


# Formulaire d'envoi de "besoin de bénévoles"
class BesoinDeBenevolesForm(forms.ModelForm):
    class Meta:
        model = BesoinDeBenevoles
        fields = [
            'titre',
            'description',
            'degre_urgence',
            'duree',
            'nombre_de_benevoles',
            'competences_demandees',
        ]

        labels = {
            'titre': 'Donnez un titre à ce besoin',
            'description': 'Description',
            'degre_urgence': 'Degré d\'urgence',
            'duree': 'Durée',
            'nombre_de_benevoles': 'Nombre de bénévoles',
            'competences_demandees': 'Compétences demandées',
        }

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'duree': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'number'}),
            'nombre_de_benevoles': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'min': '1'}),
            'competences_demandees': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': '4'}),
        }
