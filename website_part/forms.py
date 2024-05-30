from django import forms
from django.utils.safestring import mark_safe

# from website_part.models import Contact
from website_part.models import Message


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'type': 'email',
            'autocomplete': 'email',
            'class': 'form-control form-control-lg',
            'placeholder': 'Adresse e-mail'
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control form-control-lg',
            'placeholder': 'Mot de passe'
        })
    )

'''
class ContactForm(forms.Form):
    class Meta:
        model = Contact

        fields = [
            'prenom',
            'nom',
            'email',
            'telephone',
            'message'
        ]

        widget = {
            'prenom': forms.TextInput(attrs={'class': 'form-control form-control-lg danger', 'required': 'required'}),
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg danger', 'required': 'required'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control form-control-lg danger', 'required': 'required'}),
            'telephone': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control form-control-lg'}),
            'message': forms.Textarea(attrs={'class': 'form-control form-control-lg danger', 'rows': '3', 'required': 'required'})
        }

        labels = {
            'prenom': 'Prénom(s)',
            'nom': 'Nom(s)',
            'email': 'Email',
            'telephone': 'Téléphone',
            'message': 'Message'
        }
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        print(self.fields.keys())
        self.fields['prenom'].label = self.add_required_span('Prénom(s)')
        self.fields['nom'].label = self.add_required_span('Nom(s)')
        self.fields['email'].label = self.add_required_span('Email')
        self.fields['message'].label = self.add_required_span('Message')

    def add_required_span(self, label):
        return mark_safe(f'{label} <span class="danger">*</span>')
'''

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'prenom',
            'nom',
            'email',
            'telephone',
            'message'
        ]
        labels = {
            'prenom': 'Prénom(s)',
            'nom': 'Nom(s)',
            'email': 'Email',
            'telephone': 'Téléphone',
            'message': 'Message'
        }
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'required': 'required'}),
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'required': 'required'}),
            'telephone': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control form-control-lg', 'required': 'required'}),
            'message': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': '3', 'required': 'required'})
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.add_required_span()

    def add_required_span(self):
        for field_name, field in self.fields.items():
            if 'required' in field.widget.attrs:
                self.fields[field_name].label = mark_safe(f'{self.fields[field_name].label} <span class="danger">*</span>')
