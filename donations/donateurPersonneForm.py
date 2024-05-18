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
        
        fields = ['nom', 'prenom', 'email', 'telephone', 'pays', 'ville', 'genre', 'photo', 
                  'date_naissance', 'password']
        

        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'email': 'Email',
            'telephone': 'Télephone',
            'photo': 'Ajouter un profil',
            'pays': 'Pays',
            'ville': 'Ville',
            'genre': 'Genre',
            'date_naissance': 'Date de naissance',
        }

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'genre': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'pays': CountrySelectWidget(attrs={'class': 'form-select form-select-lg'}),
            'ville': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.", code='password_mismatch')

