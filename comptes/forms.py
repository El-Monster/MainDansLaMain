from django import forms
from .models import UtilisateurPersonnalise

class UtilisateurForm(forms.ModelForm):
    password_confirmation = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
    label='Confirmer le mot de passe'
    )
    
    class Meta:
        model = UtilisateurPersonnalise
        # Spécification des champs à inclure dans le formulaire
        fields = ['email', 'telephone', 'pays', 'ville', 'photo','nom','password',]
        # Définition des étiquettes pour chaque champ
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'pays': forms.Select(attrs={'class': 'form-select'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'password_confirmation': forms.PasswordInput(attrs={'class': 'form-control'})
        }
        labels = {
            'email': 'Adresse e-mail',
            'telephone': 'Téléphone',
            'pays': 'Pays',
            'ville': 'Ville',
            'photo': 'Photo de profil',
            'nom':"Nom",
            'password':"Mot de pass"
        }
        # Utilisation des widgets pour personnaliser l'apparence de certains champs
        # widgets = {

        #     'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        # }


