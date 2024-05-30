# Dans forms.py de votre application
from django import forms
from .models import DonationMaterielle

class DonationMaterielleForm(forms.ModelForm):
    class Meta:
        model = DonationMaterielle
        fields = ['categorie', 'quantite', 'description', 'date_reception', 'image']
        labels = {
            'categorie': 'Catégorie de la donation',
            'quantite': 'Quantité',
            'description': 'Description',
            'date_reception': 'Date de disponibilité',
            
            'image': 'Image'
        }
        
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date_reception': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'statut': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
