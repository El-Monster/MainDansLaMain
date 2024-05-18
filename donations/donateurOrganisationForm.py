from django import forms
from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe
from .models import DonateurOrganisation

class DonateurOrganisationForm(forms.ModelForm):
    class Meta:
        model = DonateurOrganisation
        fields = ['photo','nom', 'numero_fiscal', 'statut_juridique', 'date_creation', 
                  'email', 'telephone', 'pays', 'ville', 'type_donateur', 
                  'preferences_besoins', 'password']

        widgets = {
            'date_creation': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
        }
