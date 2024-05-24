from django import forms


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