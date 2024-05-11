from django import forms
from .models import UtilisateurPersonnalise

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = UtilisateurPersonnalise
        # Spécification des champs à inclure dans le formulaire
        fields = ['email', 'telephone', 'pays', 'ville', 'photo']
        # Définition des étiquettes pour chaque champ
        labels = {
            'email': 'Adresse e-mail',
            'telephone': 'Téléphone',
            'pays': 'Pays',
            'ville': 'Ville',
            'photo': 'Photo de profil',
        }
        # Utilisation des widgets pour personnaliser l'apparence de certains champs
        widgets = {

            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
