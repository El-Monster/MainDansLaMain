from django import forms
from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe
from .models import DonateurEntreprise


class DonateurEntrepriseForm(forms.ModelForm):
    class Meta:
        model = DonateurEntreprise
        fields = [
            #'type_donateur',
            'preferences_besoins',
            'statut',
            'numero_fiscal',
            'statut_juridique',
            'date_creation',
        ]

        widgets = {
            'numero_fiscal': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
           'statut_juridique': forms.TextInput(attrs={'class': 'form-control'}),
           'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            
        }
        
