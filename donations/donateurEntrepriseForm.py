from django import forms
from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe
from .models import DonateurEntreprise


class DonateurEntrepriseForm(forms.ModelForm):
     password_confirmation = forms.CharField(
     widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
     label='Confirmer le mot de passe'
     )
     class Meta:
        model = DonateurEntreprise
        fields = [
            'email', 'telephone', 
            'pays', 'ville', 'photo',
            'nom','password',
            
            'preferences_besoins',
            'statut',
            'numero_fiscal',
            'statut_juridique',
            'date_creation',
        ]

        widgets = {
            'numero_fiscal': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
           'statut_juridique': forms.TextInput(attrs={'class': 'form-control'}),
           'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
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