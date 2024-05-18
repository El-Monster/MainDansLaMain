from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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

def besoins(request: HttpRequest) -> HttpResponse:
    context = {'active_page': 'envoyer_besoin'}
    return render(request, 'website_part/envoyer_besoin.html', context)

def donations(request: HttpRequest) -> HttpResponse:
    context = {'active_page': 'faire_donation'} 
    return render(request, 'website_part/faire_donation.html', context)

def contactez_nous(request: HttpRequest) -> HttpResponse:
    context = {'active_page': 'contactez_nous'} 
    return render(request, 'website_part/contactez_nous.html', context)

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
    # context = {'active_page': 'se_connecter'} 
    # return render(request, 'website_part/se_connecter.html', context)