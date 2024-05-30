from django import forms
from .models import DonateurPersonne, DonateurOrganisation, DonateurEntreprise, DonationMaterielle, Visiteur


class DonateurPersonneForm(forms.ModelForm):
     password_confirmation = forms.CharField(
     widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
     label='Confirmer le mot de passe'
     )
     class Meta:
        model = DonateurPersonne
        
        widgets = {
            'preferences_besoins': forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
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
            'password_confirmation': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        }
        
        labels = {
            'prenom': 'Prénom',
            'nom':'Nom',
            'genre': 'Genre',
            'date_naissance': 'Date de naissance',
            'preferences_besoins': 'Preferences Besoins',
            'email': 'Adresse e-mail',
            'telephone': 'Téléphone',
            'pays': 'Votre pays d\'origine',
            'ville': 'Votre ville d\'origine',
            'photo': 'Choisissez votre photo de profil',
            'password': 'Mot de passe'
        }
        
        fields = [
            'preferences_besoins',
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


class DonateurOrganisationForm(forms.ModelForm):
    password_confirmation = forms.CharField(
        widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        label='Confirmer le mot de passe'
    )
    class Meta:
        model = DonateurOrganisation
        labels = {
            'numero_MATD': 'Identifiant de MATD',
            'statut_juridique': 'Statut jurique',
            'date_creation': 'Date de creation',
            'email': 'Adresse e-mail',
            'telephone': 'Téléphone',
            'pays': 'Pays',
            'ville': 'Ville',
            'photo': 'Photo de profil',
            'nom':"Nom",
            'password':"Mot de pass"
        }
        fields = [
            'numero_MATD',
            'statut_juridique',
            'date_creation',
           'email', 'telephone', 'pays',
           'ville', 'photo','nom','password'
        ]
        widgets = {
            'numero_MATD': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'statut_juridique': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg'}),
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'tel'}),
            'pays': forms.Select(attrs={'class': 'form-select form-select-lg pays', 'id': 'pays', 'onchange': 'chargerVilles()'}),
            'ville': forms.Select(attrs={'class': 'form-select form-select-lg villes', 'id': 'villes'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'password_confirmation': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        }


class DonateurEntrepriseForm(forms.ModelForm):
    password_confirmation = forms.CharField(
        widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        label = 'Confirmer le mot de passe'
    )
    class Meta:
        model = DonateurEntreprise
        fields = [
            'email',
            'telephone', 
            'pays',
            'ville',
            'photo',
            'nom',
            'password',
            'preferences_besoins',
            'statut',
            'numero_fiscal',
            'statut_juridique',
            'date_creation',
        ]

        widgets = {
            'numero_fiscal': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'statut_juridique': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg'}),
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'tel'}),
            'pays': forms.Select(attrs={'class': 'form-select form-select-lg pays', 'id': 'pays', 'onchange': 'chargerVilles()'}),
            'ville': forms.Select(attrs={'class': 'form-select form-select-lg villes', 'id': 'villes'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'password_confirmation': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        }
        
        labels = {
            'statut_juridique': 'Statut jurique de l\'entreprise',
            'date_creation': 'Date de création de l\'entreprise',
            'email': 'Email de l\'entreprise',
            'telephone': 'Téléphone de votre entreprise',
            'pays': 'Pays',
            'ville': 'Ville',
            'photo': 'Photo de profil ou logo de l\'entreprise',
            'nom':"Nom de l'entreprise",
            'password':"Mot de passe"
        }


class VisiteurForm(forms.ModelForm):
    class Meta:
        model = Visiteur
        fields = ['nom', 'prenom', 'email', 'genre', 'pays', 'ville', 'date_naissance', 'telephone']
        
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'email': 'Email',
            'genre': 'Genre',
            'pays': 'Pays',
            'ville': 'Ville',
            'date_naissance': 'Date de naissance',
            'telephone': 'Téléphone',
        }

        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'genre': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control  form-control-lg'}),    
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'tel'}),
            'pays': forms.Select(attrs={'class': 'form-select form-select-lg pays', 'id': 'pays', 'onchange': 'chargerVilles()'}),
            'ville': forms.Select(attrs={'class': 'form-select form-select-lg villes', 'id': 'villes'}),
        }


class DonationMaterielleForm(forms.ModelForm):
    class Meta:
        model = DonationMaterielle
        fields = ['categorie', 'quantite', 'description', 'date_reception', 'image']
        labels = {
            'categorie': 'Catégorie de la donation',
            'quantite': 'Quantité',
            'description': 'Description',
            'date_reception': 'Date de disponibilité',
            
            'image': 'Image'
        }
        
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date_reception': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'statut': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }