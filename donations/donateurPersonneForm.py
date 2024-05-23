from django import forms
from .models import DonateurPersonne
from django_countries.widgets import CountrySelectWidget

class DonateurPersonneForm(forms.ModelForm):
     password_confirmation = forms.CharField(
     widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
     label='Confirmer le mot de passe'
     )
     class Meta:
        model = DonateurPersonne
        
        widgets = {
            'preferences_besoins': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
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
            'prenom': 'Prénom',
            'genre': 'Genre',
            'date_naissance': 'Date de naissance',
            'preferences_besoins':"Preferences Besoins",
            'email': 'Adresse e-mail',
            'telephone': 'Téléphone',
            'pays': 'Pays',
            'ville': 'Ville',
            'photo': 'Photo de profil',
            'nom':"Nom",
            'password':"Mot de pass"
        }
        
        fields = [
            
            'preferences_besoins',
            'prenom',
            'genre',
            'date_naissance',
             'email', 'telephone', 'pays',
             'ville', 'photo','nom','password'
        ]
        
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     password_confirmation = cleaned_data.get('password_confirmation')

    #     if password and password_confirmation and password != password_confirmation:
    #         raise forms.ValidationError("Les mots de passe ne correspondent pas.", code='password_mismatch')

