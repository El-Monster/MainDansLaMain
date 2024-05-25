from django import forms
from .models import NecessiteuxPersonne

class NecessiteuxPersonneForm(forms.ModelForm):
     password_confirmation = forms.CharField(
     widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
     label='Confirmer le mot de passe'
     )
     class Meta:
        model = NecessiteuxPersonne
        fields = [
            #'type_necessiteux',
            'prenom',
            'genre',
            'date_naissance','email', 
            'telephone', 'pays', 'ville', 'photo','nom','password'
            
        ]
        
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'pays': forms.Select(attrs={'class': 'form-select'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'password_confirmation': forms.PasswordInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
        labels = {
            'prenom': 'Prénom',
            'genre': 'Genre',
            'date_naissance': 'Date de naissance',
        }
        