from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from comptes.forms import UtilisateurForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from .benevoleForm import BenevoleForm
# Create your views here.
def compte_benevole(request):
    if request.method == 'POST':
        form = BenevoleForm(request.POST)
        userForm = UtilisateurForm(request.POST, request.FILES)
        print(form.is_valid(),userForm.is_valid())
        if form.is_valid() and userForm.is_valid():
            email = userForm.cleaned_data.get('email')
            password = userForm.cleaned_data.get('password')
            User = get_user_model()
            # Vérifier si le compte email existe déjà dans la base de données
            # if User.objects.filter(email=email).exists():
            #     messages.error(request, 'Cet email a déjà un compte.')
            # elif not is_secure_password(password):
            #     messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
            # else:
            hashed_password = make_password(password)
            user = userForm.save(commit=False)
            user.password = hashed_password
            # Attribution du role
            user.role = settings.BENEVOLE
            user.save()
            benevole = form.save(commit=False)
            #benevole.type_donateur = 'individu'
            benevole.user = user
            print(benevole)
            benevole.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:index')
        else:
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'benevole/benevole.html', {'form': form, 'userForm': userForm})
    else:
        userForm = UtilisateurForm()
        form = BenevoleForm()
        
    return render(request, 'benevole/benevole.html', {'form': form, 'userForm': userForm})

