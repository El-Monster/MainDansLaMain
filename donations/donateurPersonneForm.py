from django import forms
from .models import DonateurPersonne

class DonateurPersonneForm(forms.ModelForm):
    class Meta:
        model = DonateurPersonne
        
        fields = ['nom', 'prenom', 'email', 'telephone', 'pays', 'ville', 'genre', 
                  'date_naissance', 'type_donateur', 'preferences_besoins','password']

        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput()
        }
