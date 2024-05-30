from django import forms
from .models import NecessiteuxPersonne

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
        