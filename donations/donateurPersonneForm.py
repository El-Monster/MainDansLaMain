from django import forms
from .models import DonateurPersonne
from django_countries.widgets import CountrySelectWidget

class DonateurPersonneForm(forms.ModelForm):
    class Meta:
        model = DonateurPersonne
        
        widgets = {
            'preferences_besoins': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # 'type_donateur': forms.Select(attrs={'class': 'form-select'}),
        }
        
        labels = {
            'prenom': 'Prénom',
            'genre': 'Genre',
            'date_naissance': 'Date de naissance',
            # 'type_donateur': 'Type de donateur',
            'preferences_besoins':"Preferences Besoins"
        }
        
        fields = [
            # 'type_donateur',
            'preferences_besoins',
            'prenom',
            'genre',
            'date_naissance',
            # 'type_donateur'
        ]
        
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     password_confirmation = cleaned_data.get('password_confirmation')

    #     if password and password_confirmation and password != password_confirmation:
    #         raise forms.ValidationError("Les mots de passe ne correspondent pas.", code='password_mismatch')

