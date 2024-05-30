# forms.py
from django import forms
from .models import BesoinMateriel, BesoinFinancier,BesoinDeBenevoles

class BesoinMaterielForm(forms.ModelForm):
    class Meta:
        model = BesoinMateriel
        fields = [
            'titre',
            'description',
            'degre_urgence',
            'image',
            'document',
            'video',
            'categorie',
            'quantite',
        ]

        labels = {
            'titre': 'Titre du besoin',
            'description': 'Description du besoin',
            'categorie': 'Catégorie',
            'quantite': 'Quantité',
            'degre_urgence': 'Degré d\'urgence',
            'image': 'Image associée',
            'document': 'Document associé',
            'video': 'Vidéo associée',
        }

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': '4'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'min': '1'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'document': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'video': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'categorie': forms.Select(attrs={'class': 'form-select form-select-lg'}),
        }

class BesoinFinancierForm(forms.ModelForm):
    class Meta:
        model = BesoinFinancier
        
        fields = [
            'titre',
            'description',
            'degre_urgence',
            'image',
            'document',
            'video',
            'montant_souhaite',
        ]

        labels = {
            'titre': 'Titre du besoin',
            'description': 'Description du besoin',
            'degre_urgence': 'Degré d\'urgence',
            'montant_souhaite': 'Montant Nécessaire',
            'image': 'Image associée',
            'document': 'Document associé',
            'video': 'Vidéo associée',
        }

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': '4'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'document': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'video': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'type': 'file'}),
            'montant_souhaite': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }


#cette partie cree le formulaire  de formulaire
class BesoinDeBenevolesForm(forms.ModelForm):
    class Meta:
        model = BesoinDeBenevoles
        fields = [
            'titre',
            'description',
            'degre_urgence',
            'duree',
            'nombre_de_benevoles',
            'competences_demandees',
        ]

        labels = {
            'titre': 'Donnez un titre à ce besoin',
            'description': 'Description',
            'degre_urgence': 'Degré d\'urgence',
            'duree': 'Durée',
            'nombre_de_benevoles': 'Nombre de bénévoles',
            'competences_demandees': 'Compétences demandées',
        }

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'duree': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'number'}),
            'nombre_de_benevoles': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'min': '1'}),
            'competences_demandees': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': '4'}),
        }
