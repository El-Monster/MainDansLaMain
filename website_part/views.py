from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .besoinForm import BesoinMaterielForm, BesoinFinancierForm,BesoinDeBenevolesForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BesoinMateriel,BesoinFinancier
from django.conf import settings
from website_part.forms import LoginForm

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {'active_page': 'index'}
    return render(request, 'website_part/index.html', context)

def a_propos(request: HttpRequest) -> HttpResponse:
    context = {'active_page': 'a_propos'}
    return render(request, 'website_part/a_propos.html', context)

def actions(request: HttpRequest) -> HttpResponse:
    context = {'active_page': 'nos_actions'}
    return render(request, 'website_part/nos_actions.html', context)

"""
    def besoins(request: HttpRequest) -> HttpResponse:
        context = {'active_page': 'envoyer_besoin'}
        return render(request, 'website_part/envoyer_besoin.html', context)
"""
def donations(request: HttpRequest) -> HttpResponse:
    context = {'active_page': 'faire_donation'} 
    return render(request, 'website_part/faire_donation.html', context)

def contactez_nous(request: HttpRequest) -> HttpResponse:
    context = {'active_page': 'contactez_nous'} 
    return render(request, 'website_part/contactez_nous.html', context)

#cette vue permet l'authentifiaction
def se_connecter(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Vous êtes connecté avec succès.')
                if(user.role == settings.PERSONNE_DONATEUR):
                    return redirect('website_part:contactez_nous')
                return redirect('website_part:index')
            else:
                messages.error(request, 'Email ou mot de passe incorrect.')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = LoginForm()
    return render(request, 'website_part/se_connecter.html', {'form': form})
#cette vue permet de creer u n besoin materiel


def creer_besoin_materiel(request):
    if request.method == 'POST':
        form = BesoinMaterielForm(request.POST, request.FILES)
        if form.is_valid():
            besoin_materiel = form.save(commit=False)
            besoin_materiel.statut = 'En attente'
            besoin_materiel.type = 'Materiel'
            besoin_materiel.save()
            messages.success(request, 'Votre besoin matériel a été soumis avec succès et est en attente de validation.')
            return redirect('website_part:besoinMateriel_page')
        else:
            messages.error(request, 'Il y a eu une erreur dans le formulaire. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = BesoinMaterielForm()
    return render(request, 'website_part/envoyer_besoin.html', {'form': form})

def creer_besoin_financier(request):
    if request.method == 'POST':
        form = BesoinFinancierForm(request.POST, request.FILES)
        if form.is_valid():
            besoin_financier = form.save(commit=False)
            besoin_financier.statut = 'En attente'
            besoin_financier.type = 'Financier'
            besoin_financier.save()
            messages.success(request, 'Votre besoin financier a été soumis avec succès et est en attente de validation.')
            return redirect('website_part:besoinFinancier_page')
        else:
            messages.error(request, 'Il y a eu une erreur dans le formulaire. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = BesoinFinancierForm()
    return render(request, 'website_part/besoinFinancier.html', {'form': form})
#cette vue permet de lister les besoins de en attente
def besoins_en_attente(request):
    besoins = BesoinMateriel.objects.filter(statut='En attente')
    if not besoins:
        messages.info(request, 'Il n\'y a pas de besoins matériels en attente.')
    return render(request, 'website_part/besoins_en_attente.html', {'besoins': besoins})

#cette vue permet d'envoyer un besoin de benevoles

def creer_besoin_benevoles(request):
    if request.method == 'POST':
        form = BesoinDeBenevolesForm(request.POST)
        if form.is_valid():
            besoin_benevoles = form.save(commit=False)
            besoin_benevoles.statut = 'En attente'
            besoin_benevoles.type = 'Bénévoles'
            besoin_benevoles.save()
            messages.success(request, 'Votre besoin de bénévoles a été soumis avec succès et est en attente de validation.')
            return redirect('website_part:besoinBenevoles_page')
        else:
            messages.error(request, 'Il y a eu une erreur dans le formulaire. Veuillez corriger les erreurs ci-dessous.')
    else:
        
        form = BesoinDeBenevolesForm()
    return render(request, 'website_part/besoinBenevoles.html', {'form': form})

