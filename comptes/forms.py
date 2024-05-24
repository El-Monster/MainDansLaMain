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
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'tel'}),
            'pays': forms.Select(attrs={'class': 'form-select form-select-lg pays', 'id': 'pays', 'onchange': 'chargerVilles()'}),
            'ville': forms.Select(attrs={'class': 'form-select form-select-lg villes', 'id': 'villes'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'password_confirmation': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        }
        labels = {
            'email': 'Adresse e-mail',
            'telephone': 'Téléphone',
            'pays': 'Votre pays d\'origine',
            'ville': 'Votre ville d\'origine',
            'photo': 'Photo de profil',
            'nom':"Nom",
            'password':"Mot de pass"
        }
        # Utilisation des widgets pour personnaliser l'apparence de certains champs
        # widgets = {

        #     'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        # }


