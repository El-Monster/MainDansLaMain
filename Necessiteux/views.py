from django.shortcuts import render,redirect
#from comptes.forms import UtilisateurForm
from .necessiteuxPersonneForm import NecessiteuxPersonneForm
from .necessiteuxOrganisationForm import NecessiteuxOrganisationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.conf import settings

#creation des vues  de creations de comptes de necessiteux
def necessiteuxPersonne(request):
    if request.method == 'POST':
        form = NecessiteuxPersonneForm(request.POST,request.FILES)
        #userForm = UtilisateurForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid() :
            #email = userForm.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User = get_user_model()
            # Vérifier si le compte email existe déjà dans la base de données
            # if User.objects.filter(email=email).exists():
            #     messages.error(request, 'Cet email a déjà un compte.')
            # elif not is_secure_password(password):
            #     messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
            # else:
            hashed_password = make_password(password)
            user =form.save(commit=False)
            user.password = hashed_password
            # Attribution du role
            user.role = settings.PERSONNE_NECESSITEUX
            #user.save()
            necessiteux = form.save(commit=False)
            necessiteux.type_necessiteux = 'Personne'
            necessiteux.user = user
            print(necessiteux)
            necessiteux.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:index')
        else:
            form = NecessiteuxPersonneForm()
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'Necessiteux/NecessiteuxPersonne.html', {'form': form})
    else:
        #userForm = UtilisateurForm()
        form = NecessiteuxPersonneForm()
    return render(request, 'Necessiteux/NecessiteuxPersonne.html', {'form': form})

    



def necessiteuxOrganisation(request):
    if request.method == 'POST':
        form = NecessiteuxOrganisationForm(request.POST,request.FILES)
        
        print(form.is_valid())
        if form.is_valid() :
            email =form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User = get_user_model()
            # Vérifier si le compte email existe déjà dans la base de données
            # if User.objects.filter(email=email).exists():
            #     messages.error(request, 'Cet email a déjà un compte.')
            # elif not is_secure_password(password):
            #     messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
            # else:
            hashed_password = make_password(password)
            user = form.save(commit=False)
            user.password = hashed_password
            # Attribution du role
            user.role = settings.ORGANISATION_NECESSITEUX
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
            return render(request, 'Necessiteux/necessiteuxOrganisation.html', {'form': form})
    else:
        
        form = NecessiteuxOrganisationForm()
    return render(request, 'Necessiteux/NecessiteuxOrganisation.html', {'form': form})
