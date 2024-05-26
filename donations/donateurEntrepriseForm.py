from django import forms
from .models import DonateurEntreprise


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