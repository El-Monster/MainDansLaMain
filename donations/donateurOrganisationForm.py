from django import forms
from .models import DonateurOrganisation

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