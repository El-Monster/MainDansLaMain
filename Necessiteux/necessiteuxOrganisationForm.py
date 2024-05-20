from django import forms
from .models import NecessiteuxOrganisation

class NecessiteuxOrganisationForm(forms.ModelForm):
    
    class Meta:
        model = NecessiteuxOrganisation
        fields = [
            'numero_matd',
            'agrement_maspfe',
            'statut_juridique',
            'date_creation',
        ]
        widgets = {
            'numero_matd': forms.TextInput(attrs={'class': 'form-control'}),
            'statut_juridique': forms.Select(attrs={'class': 'form-control'}),
            'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'agrement_maspfe': forms.TextInput(attrs={'class': 'form-control'})
            
        }
          
        labels = {
            'numero_matd': 'Numéro MATD',
            'agrement_maspfe': 'Agrément MASFE',
            'statut_juridique': 'Statut juridique',
            'date_creation': 'Date de création', 
            
        }