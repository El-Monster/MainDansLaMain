# forms.py
from django import forms
from .models import BesoinMateriel, BesoinFinancier,BesoinDeBenevoles 
class BesoinMaterielForm(forms.ModelForm):
    class Meta:
        model = BesoinMateriel
        fields = [ 'necessiteux','titre', 'description', 'degre_urgence', 'date_limite',  'image', 'document', 'video',  'categorie', 'quantite']
        labels = {
            'necessiteux':'Personne en besoin',
            'titre': 'Titre du besoin',
            'description': 'Description du besoin',
            'degre_urgence': 'Degré d\'urgence',
            'statut': 'Statut du besoin',
            'image': 'Image associée',
            'document': 'Document associé',
            'video': 'Vidéo associée',
            'categorie': 'Catégorie',
            'quantite': 'Quantité',
        }
        widgets = {
            'necessiteux': forms.Select(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'date_limite': forms.DateTimeInput(attrs={'class': 'form-control form-control-lg', 'type': 'datetime-local'}),
            'statut': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'type': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg'}),
            'montant_souhaite': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'categorie': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }

class BesoinFinancierForm(forms.ModelForm):
    class Meta:
        model = BesoinFinancier
        fields = [ 'necessiteux','titre', 'description', 'degre_urgence', 'date_limite', 'image', 'document', 'video', 'montant_souhaite']
        labels = {
             'necessiteux':'Personne en besoin',
            'titre': 'Titre du besoin',
            'description': 'Description du besoin',
            'degre_urgence': 'Degré d\'urgence',
            'image': 'Image associée',
            'document': 'Document associé',
            'video': 'Vidéo associée',
            'montant_souhaite': 'Montant Necessaire',
            
        }
        widgets = {
            'necessiteux': forms.Select(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control-'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'montant_souhaite': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
#cette partie cree le formulaire  de formulaire



class BesoinDeBenevolesForm(forms.ModelForm):
    class Meta:
        model = BesoinDeBenevoles
        fields = ['titre', 'description', 'degre_urgence', 'duree', 'nombre_de_benevoles', 'competences_demandees','necessiteux']
        labels = {
            'necessiteux':'Necessiteux ',
            'titre': 'Titre',
            'description': 'Description',
            'degre_urgence': 'Degré d\'urgence',
            'duree': 'Durée',
            'nombre_de_benevoles': 'Nombre de bénévoles',
            'competences_demandees': 'Compétences demandées',
        }
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'degre_urgence': forms.Select(attrs={'class': 'form-control'}),
            'duree': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_benevoles': forms.NumberInput(attrs={'class': 'form-control'}),
            'competences_demandees': forms.Textarea(attrs={'class': 'form-control'}),
            'necessiteux': forms.Select(attrs={'class': 'form-control'}),
        }
