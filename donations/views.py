from django.shortcuts import render,redirect
from .donateurPersonneForm import DonateurPersonneForm
from .donateurOrganisationForm import DonateurOrganisationForm
from .donateurEntrepriseForm import DonateurEntrepriseForm
from django.http import HttpResponse
from .models import DonateurEntreprise
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.
#creation de la vue pour la page de don
def donateurPersonne(request):
    if request.method == 'POST':
        form = DonateurPersonneForm(request.POST)
        if form.is_valid():
            donateur_personne = form.save()
            # Redirection vers une autre vue ou une autre URL après avoir enregistré le donateur
            return redirect('')
    else:
        form = DonateurPersonneForm()
    return render(request, 'donations/donateurPersonne.html', {'form': form})


def donateurOrganisation(request):
    if request.method == 'POST':
        form =  DonateurOrganisationForm(request.POST)
        if form.is_valid():
            donateur_organisation = form.save()
            # Redirection vers une autre vue ou une autre URL après avoir enregistré le donateur
            return redirect('')
    else:
        form = DonateurOrganisationForm()
    return render(request, 'donations/donateurOrganisation.html', {'form': form})


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
    error_message = None  # Initialisez le message d'erreur à None

    if request.method == 'POST':
        form = DonateurEntrepriseForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User = get_user_model()
            # Vérifier si le compte email existe déjà dans la base de données
            if User.objects.filter(email=email).exists():
                messages.add_message(request,messages.ERROR,'cet Email a deja un compte')
                return render(request,'donations/donateurEntreprise.html',{'messages':messages.get_messages(request)})
            if not is_secure_password(password):
                messages.add_message(request,messages.ERROR,'le mot de pass ne correspond pas au critere de securité')
                return render(request,'donations/donateurEntreprise.html',{'messages':messages.get_messages(request)})   
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Votre compte a été crée avec succes.')
            return render(request,'donations/donateurEntreprise.html',{'messages':messages.get_messages(request)})
            # return redirect('donations:donateurEntreprise_compte')
        else:
           messages.add_message(request,messages.ERROR,"Il y a des erreurs dans le formulaire. Veuillez corriger et réessayer.")
           return render(request,'donations/donateurEntreprise.html',{'messages':messages.get_messages(request)})
    else:
        form = DonateurEntrepriseForm()
    return render(request, 'donations/donateurEntreprise.html', {'form': form, 'error_message': error_message})

# cette vue permet d'afficher la page d'accueil pour la creation des comptes des differents donateurs
def donateurcompte(request):
        return render(request,'donations/donateurcompte.html')