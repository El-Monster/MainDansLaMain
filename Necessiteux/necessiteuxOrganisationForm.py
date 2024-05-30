from django import forms
from .models import NecessiteuxOrganisation

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