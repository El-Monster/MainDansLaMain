from django import forms
from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe
from .models import DonateurOrganisation

"""class ImagePreviewWidget(ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        default_image_url = 'chemin/vers/votre/image/par/defaut.jpg'
        if not value:
            html += f'<br><img src="{default_image_url}" style="max-height: 100px;">'
        elif value and hasattr(value, 'url'):
            html += f'<br><img src="{value.url}" style="max-height: 100px;">'
        return mark_safe(html)
"""
class DonateurOrganisationForm(forms.ModelForm):
    class Meta:
        model = DonateurOrganisation
        fields = ['photo','nom', 'numero_fiscal', 'statut_juridique', 'date_creation', 
                  'email', 'telephone', 'pays', 'ville', 'type_donateur', 
                  'preferences_besoins', 'password']

        widgets = {
            'date_creation': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
            'photo': forms.ImageField()
        }
