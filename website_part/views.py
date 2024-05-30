import smtplib
from django.core.mail import send_mail
from django.core.mail import send_mail, BadHeaderError
from django.core.mail.backends.base import BaseEmailBackend

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from Necessiteux.models import Necessiteux, NecessiteuxOrganisation, NecessiteuxPersonne
from benevole.models import Benevole
from donations.models import Donateur, DonateurEntreprise, DonateurOrganisation, DonateurPersonne
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from website_part.forms import LoginForm, MessageForm

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
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # form.save()

            # Préparer l'email
            subject = 'Nouveau message de contact'
            message = f"""
                Prénom: {form.cleaned_data['prenom']}
                Nom: {form.cleaned_data['nom']}
                Email: {form.cleaned_data['email']}
                Téléphone: {form.cleaned_data['telephone']}
                Message: {form.cleaned_data['message']}
            """
            # from_email = settings.DEFAULT_FROM_EMAIL
            from_email = form.cleaned_data['email']
            recipient_list = settings.DEFAULT_TO_EMAIL

            print('envoyeur : ', from_email, 'receveur : ', recipient_list)

            # Envoyer l'email
            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Votre message a été envoyé avec succès.')
            except BadHeaderError:
                messages.error(request, 'Entête d\'email invalide détectée.')
            except smtplib.SMTPException as e:
                messages.error(request, f'Échec de l\'envoi de l\'email :\n{str(e)}')
                print(f'erreur : {str(e)}')
            except Exception as e:
                messages.error(request, f'Une erreur est survenue : {str(e)}')
            
            return redirect('website_part:contactez_nous')
    else:
        form = MessageForm()
        context = {
            'active_page': 'contactez_nous',
            'form': form
        }
        return render(request, 'website_part/contactez_nous.html', context)


'''
    Cette vue permet l'authentifiaction'
'''
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
                context = {}

                # Si 'DONATEUR'
                if user.role == settings.DONATEUR:
                    # Récupération du donateur 
                    donateur = Donateur.objects.get(id = user.id)
                    
                    if donateur.type_donateur == settings.PERSONNE:
                        donateur_personne = DonateurPersonne.objects.get(id = user.id)
                        context['utilisateur_id'] = donateur_personne.id
                    elif donateur.type_donateur == settings.ORGANISATION:
                        donateur_organisation = DonateurOrganisation.objects.get(id = user.id)
                        context['utilisateur_id'] = donateur_organisation.id
                    else:
                        donateur_entreprise = DonateurEntreprise.objects.get(id = user.id)
                        context['utilisateur_id'] = donateur_entreprise.id
                    
                    # Stocker le contexte dans la session
                    request.session['context'] = context

                    return redirect('donations:donateurTableauBord')
                
                # Si 'NECESSITEUX'
                elif user.role == settings.NECESSITEUX:
                    necessiteux = Necessiteux.objects.get(id = user.id)

                    context['utilisateur_type'] = necessiteux.type_necessiteux

                    if necessiteux.type_necessiteux == settings.PERSONNE:
                        necessiteux_personne = NecessiteuxPersonne.objects.get(id = user.id)
                        context['utilisateur_id'] = necessiteux_personne.id
                    else:
                        necessiteux_organisation = NecessiteuxOrganisation.objects.get(id = user.id)
                        context['utilisateur_id'] = necessiteux_organisation.id

                    # Stocker le contexte dans la session
                    request.session['context'] = context
                    
                    return redirect('Necessiteux:appNecessiteuxTableauBord')
                # Si 'BENEVOLE'
                elif user.role == settings.BENEVOLE:
                    benevole = Benevole.objects.get(id = user.id)
                    context['benevole_id'] = benevole.id

                # Si 'AGENT DE COLLECTE'
                elif user.role == settings.AGENT_COLLECTE:
                    print('Agent de collecte')
                
                else:
                    print('')
                    # return render(request, '404.html', context)
            else:
                form = LoginForm()
                context = {
                    'active_page': 'se_connecter',
                    'form': form
                }
                messages.warning(request, 'Email ou mot de passe incorrect.')
                return render(request, 'website_part/se_connecter.html', context)
        else:
            form = LoginForm()
            context = {
                'active_page': 'se_connecter',
                'form': form
            }
            messages.warning(request, 'Veuillez corriger les erreurs ci-dessous.')
            return render(request, 'website_part/se_connecter.html', context)
    else:
        form = LoginForm()
    return render(request, 'website_part/se_connecter.html', {'form': form})

'''
    Cette vue permet la deconnexion 
'''
def se_deconnecter(request: HttpRequest) -> HttpResponse:
    try:
        del request.session["utilisateur_id"]
    except KeyError:
        pass
    return redirect('website_part:se_connecter')
