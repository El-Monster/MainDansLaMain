from django import forms
from .models import DonateurOrganisation

class DonateurOrganisationForm(forms.ModelForm):
    class Meta:
        model = DonateurOrganisation
        labels = {
            'numero_MATD': 'Identifiant de MATD',
            'statut_juridique': 'Statut jurique',
            'date_creation': 'Date de creation',
        }
        fields = [
            'numero_MATD',
            'statut_juridique',
            'date_creation',
           
        ]
        widgets = {
            'numero_MATD': forms.TextInput(attrs={'class': 'form-control'}),
            'statut_juridique': forms.TextInput(attrs={'class': 'form-control'}),
            'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            
        }