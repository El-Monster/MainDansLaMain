from django import forms
from .models import NecessiteuxPersonne

class NecessiteuxPersonneForm(forms.ModelForm):
    
    class Meta:
        model = NecessiteuxPersonne
        fields = [
            'nom',
            'type_necessiteux',
            'user',
            'prenom',
            'genre',
            'date_naissance',
        ]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'})
        }