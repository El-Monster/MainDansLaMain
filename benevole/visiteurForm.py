from django import forms
from donations.models import Visiteur

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
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'pays': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }
