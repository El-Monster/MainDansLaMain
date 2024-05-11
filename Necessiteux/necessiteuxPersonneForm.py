from django import forms
from .models import NecessiteuxPersonne

class NecessiteuxPersonneForm(forms.ModelForm):
    
    class Meta:
        model = NecessiteuxPersonne
        fields = ['nom', 'prenom', 'email', 'telephone', 'pays', 'ville', 'genre', 'date_naissance', 'photo','type_necessiteux']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'})
        }