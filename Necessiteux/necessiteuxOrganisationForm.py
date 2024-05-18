from django import forms
from .models import NecessiteuxOrganisation

class NecessiteuxOrganisationForm(forms.ModelForm):
    
    class Meta:
        model = NecessiteuxOrganisation
        fields = [
            'nom',
            'type_necessiteux',
            'numero_matd',
            'agrement_maspfe',
            'statut_juridique',
            'date_creation',
        ]
        widgets = {
            'date_creation': forms.DateInput(attrs={'type': 'date'})
        }
          
        labels = {
            'nom': 'Nom de l\'organisation',
            'numero_matd': 'Numéro MATD',
            'agrement_maspfe': 'Agrément MASFE',
            'statut_juridique': 'Statut juridique',
            'date_creation': 'Date de création',
            'email': 'Email de l\'entreprise',
            'telephone': 'Téléphone de l\'entreprise',
            'pays': 'Pays',
            'ville': 'Ville',
            'type_necessiteux': 'Type de nécessiteux'
        }