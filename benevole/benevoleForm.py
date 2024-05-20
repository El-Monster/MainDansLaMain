from django import forms
from .models import Benevole

class BenevoleForm(forms.ModelForm):

    class Meta:
        model = Benevole
        fields = [
             'prenom',  
             'genre', 
             'date_naissance', 
             'domaines_de_competences', 
              ]

        labels = {
            
            'prenom': 'Prénom',
            'genre': 'Genre',
            'date_naissance': 'Date de naissance',
            'domaines_de_competences': 'Domaines de compétences',
            
        }

        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'domaines_de_competences': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),  # Ajustez les valeurs de 'rows' et 'cols' selon vos besoins,
            
        }

   
