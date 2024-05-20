from django.shortcuts import render,redirect
from comptes.forms import UtilisateurForm
from .necessiteuxPersonneForm import NecessiteuxPersonneForm
from .necessiteuxOrganisationForm import NecessiteuxOrganisationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.conf import settings

#creation des vues  de creations de comptes de necessiteux
def necessiteuxPersonne(request):
    if request.method == 'POST':
        form = NecessiteuxPersonneForm(request.POST)
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
            user.role = settings.PERSONNE_NECESSITEUX
            user.save()
            donateur = form.save(commit=False)
            donateur.type_donateur = 'Organisation'
            donateur.user = user
            print(donateur)
            donateur.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:index')
        else:
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'donations/donateurPersonne.html', {'form': form, 'userForm': userForm})
    else:
        userForm = UtilisateurForm()
        form = NecessiteuxPersonneForm()
    return render(request, 'Necessiteux/NecessiteuxPersonne.html', {'form': form, 'userForm': userForm})

    



def necessiteuxOrganisation(request):
    if request.method == 'POST':
        form = NecessiteuxOrganisationForm(request.POST)
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
            user.role = settings.ORGANISATION_NECESSITEUX
            
            user.save()
            donateur = form.save(commit=False)
            #attribution de type
            donateur.type_donateur = 'Organisation'
            donateur.user = user
            print(donateur)
            donateur.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:index')
        else:
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'Necessiteux/necessiteuxOrganisation.html', {'form': form, 'userForm': userForm})
    else:
        userForm = UtilisateurForm()
        form = NecessiteuxOrganisationForm()
    return render(request, 'Necessiteux/NecessiteuxOrganisation.html', {'form': form, 'userForm': userForm})
