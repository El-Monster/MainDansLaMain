from django import forms
from .models import NecessiteuxPersonne

class NecessiteuxPersonneForm(forms.ModelForm):
    
    class Meta:
        model = NecessiteuxPersonne
        fields = [
            #'type_necessiteux',
            'prenom',
            'genre',
            'date_naissance',
        ]
        
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
        labels = {
            'prenom': 'Prénom',
            'genre': 'Genre',
            'date_naissance': 'Date de naissance',
        }
        