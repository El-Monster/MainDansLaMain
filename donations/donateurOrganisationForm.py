from django import forms
from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe
from .models import DonateurOrganisation

class DonateurOrganisationForm(forms.ModelForm):
    class Meta:
        model = DonateurOrganisation
        fields = [
            'numero_MATD',
            'statut_juridique',
            'date_creation',
            'type_donateur',
            'preferences_besoins',
        ]

        widgets = {
            'date_creation': forms.DateInput(attrs={'type': 'date'})
        }
