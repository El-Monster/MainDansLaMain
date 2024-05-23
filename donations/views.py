from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from comptes.forms import UtilisateurForm

from .donateurPersonneForm import DonateurPersonneForm
from .donateurOrganisationForm import DonateurOrganisationForm
from .donateurEntrepriseForm import DonateurEntrepriseForm

from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.
#creation de la vue pour la page de don

# def donateurPersonne(request):
#     if request.method == 'POST':
#         print('EEEEE')
#         form = DonateurPersonneForm(request.POST)
#         userForm = UtilisateurForm(request.POST, request.FILES)
#         if form.is_valid() and form.is_valid():
#             email = userForm.cleaned_data.get('email')
#             password = userForm.cleaned_data.get('password')
#             User = get_user_model()
            
#             # Vérifier si le compte email existe déjà dans la base de données
#             if User.objects.filter(email=email).exists():
#                 messages.error(request, 'Cet email a déjà un compte.')
#             elif not is_secure_password(password):
#                 messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
#             else:
#                 user = userForm.save()
#                 if(form.is_valid()):
#                     donateur = form.save(commit=False)
#                     donateur.user.pk = user.pk
#                     donateur.save()
#                 messages.success(request, 'Votre compte a été créé avec succès.')
#                 return redirect('website_part:index')
#         else:
#             # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
#             return render(request, 'donations/donateurPersonne.html', {'form': form})
#     else:
#         userForm = UtilisateurForm()
#         form = DonateurPersonneForm()
#     return render(request, 'donations/donateurPersonne.html', {'form': form, "userForm":userForm})


def donateurPersonne(request):
    if request.method == 'POST':
        form = DonateurPersonneForm(request.POST,request.FILES)
        #userForm = UtilisateurForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid() :
            email = form.cleaned_data.get('email')
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
            user.role = settings.PERSONNE_DONATEUR
            
            
            donateur = form.save(commit=False)
            donateur.type_donateur = 'individu'
            donateur.user = user
            print(donateur)
            donateur.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:index')
        else:
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'donations/donateurPersonne.html', {'form': form})
    else:
        
        form = DonateurPersonneForm()
        
    return render(request, 'donations/donateurPersonne.html', {'form': form})





# cette fonction permet de mettre de la secrité dans le mot de pass
def is_secure_password(password):
    # Définir les critères de sécurité pour le mot de passe
    min_length = 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    
    # Vérifier si le mot de passe répond à tous les critères
    return (
        len(password) >= min_length and
        has_uppercase and
        has_lowercase and
        has_digit and
        has_special
    )



def donateurEntreprise(request):
    if request.method == 'POST':
        form = DonateurEntrepriseForm(request.POST,request.FILES)
        #userForm = UtilisateurForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            email = form.cleaned_data.get('email')
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
            user.role = settings.ENTREPRISE_DONATEUR
            donateur = form.save(commit=False)
            donateur.type_donateur = 'Entreprise'
            donateur.user = user
            print(donateur)
            donateur.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:index')
        else:
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'donations/donateurEntreprise.html', {'form': form})
    else:
        
        form = DonateurEntrepriseForm()
        
    return render(request, 'donations/donateurEntreprise.html', {'form': form})


def donateurOrganisation(request):
    if request.method == 'POST':
        form = DonateurOrganisationForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid() :
            email = form.cleaned_data.get('email')
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
            user.role = settings.ENTREPRISE_DONATEUR
            
           
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
            return render(request, 'donations/donateurOrganisation.html', {'form': form})
    else:
        userForm = UtilisateurForm()
        form = DonateurOrganisationForm()
        
    return render(request, 'donations/donateurOrganisation.html', {'form': form})


# cette vue permet d'afficher la page d'accueil pour la creation des comptes des differents donateurs
def donateurcompte(request):
        return render(request,'donations/donateurcompte.html')