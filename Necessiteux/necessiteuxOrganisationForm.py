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
            'date_creation','email', 'telephone', 
            'pays', 'ville', 'photo','nom','password'
        ]
        widgets = {
            'numero_matd': forms.TextInput(attrs={'class': 'form-control'}),
            'statut_juridique': forms.Select(attrs={'class': 'form-control'}),
            'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'agrement_maspfe': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'pays': forms.Select(attrs={'class': 'form-select'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'password_confirmation': forms.PasswordInput(attrs={'class': 'form-control'})
            
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
            'password':"Mot de pass"
            
        }