from django import forms


class LoginForm(forms.Form):
    # email = forms.EmailField()
    # password = forms.CharField(label="Mot de passe", strip=False)
    # class Meta:
    #     widgets = {
    #         'email': forms.EmailInput(attrs={'class': 'form-control'}),
    #         'password': forms.PasswordInput(attrs={'class': 'form-control'})
    #     }
        
    #     labels = {
    #         'email': 'Adresse email',
    #         'password': 'Mot de passe',
    #     }

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
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