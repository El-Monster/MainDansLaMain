from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect

from Necessiteux.besoinForm import BesoinDeBenevolesForm, BesoinFinancierForm, BesoinMaterielForm
from Necessiteux.models import BesoinMateriel, NecessiteuxOrganisation, NecessiteuxPersonne
from donations.views import is_secure_password
#from comptes.forms import UtilisateurForm
from .necessiteuxPersonneForm import NecessiteuxPersonneForm
from .necessiteuxOrganisationForm import NecessiteuxOrganisationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.conf import settings

#creation des vues  de creations de comptes de necessiteux
def necessiteuxPersonne(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NecessiteuxPersonneForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid() :
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User = get_user_model()

            # Vérifier si le compte email existe déjà dans la base de données
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email a déjà un compte.')
                return render(request, 'Necessiteux/NecessiteuxPersonne.html', {'form': form})
            
            if not is_secure_password(password):
                messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
                return render(request, 'Necessiteux/NecessiteuxPersonne.html', {'form': form})
            
            hashed_password = make_password(password)
            user = form.save(commit=False)
            user.password = hashed_password
            
            # Attribution du role
            user.role = settings.NECESSITEUX
            #user.save()
            
            necessiteux = form.save(commit=False)
            necessiteux.type_necessiteux = settings.PERSONNE
            necessiteux.user = user
            print(necessiteux)
            necessiteux.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:se_connecter')
        else:
            form = NecessiteuxPersonneForm()
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'Necessiteux/NecessiteuxPersonne.html', {'form': form})
    else:
        #userForm = UtilisateurForm()
        form = NecessiteuxPersonneForm()
    return render(request, 'Necessiteux/NecessiteuxPersonne.html', {'form': form})


def necessiteuxOrganisation(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NecessiteuxOrganisationForm(request.POST,request.FILES)
        
        print(form.is_valid())
        if form.is_valid() :
            email =form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User = get_user_model()
            
            # Vérifier si le compte email existe déjà dans la base de données
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email a déjà un compte.')
                return render(request, 'Necessiteux/necessiteuxOrganisation.html', {'form': form})
            
            # Vérifier si le mot de passe est sécurisé
            if not is_secure_password(password):
                messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
                return render(request, 'Necessiteux/necessiteuxOrganisation.html', {'form': form})
            
            hashed_password = make_password(password)
            user = form.save(commit=False)
            user.password = hashed_password
            
            # Attribution du role
            user.role = settings.NECESSITEUX
            donateur = form.save(commit=False)
            
            #attribution de type
            donateur.type_donateur = settings.ORGANISATION
            donateur.user = user
            print(donateur)
            donateur.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:se_connecter')
        else:
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'Necessiteux/necessiteuxOrganisation.html', {'form': form})
    else:
        
        form = NecessiteuxOrganisationForm()
    return render(request, 'Necessiteux/NecessiteuxOrganisation.html', {'form': form})

'''
# Ancien code
def appNecessiteuxTableauBord(request: HttpRequest) -> HttpResponse:
    context = request.session.get('context', {})

    # Récupérer le nécessiteux si l'ID est présent dans le contexte
    if 'utilisateur_id' in context:
        utilisateur_id = context['utilisateur_id']

        if context['utilisateur_type'] == settings.PERSONNE:
            context['utilisateur'] = NecessiteuxPersonne.objects.get(id=utilisateur_id)
        else:
            context['utilisateur'] = NecessiteuxOrganisation.objects.get(id=utilisateur_id)
    
        return render(request, 'Necessiteux/app/tableauBord.html', context)

    return HttpResponse('404')
'''
'''
    La vue qui renvoie sur le tableau de bord
'''
def appNecessiteuxTableauBord(request: HttpRequest) -> HttpResponse:
    context = getContextNecessiteux(request)

    if context is not None:
        context['page_active'] = 'tableauBord'
        return render(request, 'Necessiteux/app/tableauBord.html', context)
    
    return HttpResponse('404')

'''
    La vue qui renvoie sur la page des besoins
'''
def appNecessiteuxBesoins(request: HttpResponse) -> HttpResponse:
    context = getContextNecessiteux(request)

    if context is not None:
        context['page_active'] = 'besoins'
        return render(request, 'Necessiteux/app/besoins.html', context)

    return HttpResponse('404')

'''
    Méthode qui permet de récupérer les informations du nécessiteux
    en fonction de son identifiant passé en session dans la requête.
'''
def getContextNecessiteux(request) -> dict | None:
    context = request.session.get('context', {})

    # Récupérer le nécessiteux si l'ID est présent dans le contexte
    if 'utilisateur_id' in context:
        utilisateur_id = context['utilisateur_id']

        if context['utilisateur_type'] == settings.PERSONNE:
            context['utilisateur'] = NecessiteuxPersonne.objects.get(id=utilisateur_id)
        else:
            context['utilisateur'] = NecessiteuxOrganisation.objects.get(id=utilisateur_id)
    
        return context
    
    return None

'''
    Page pour la création d'un nouveau "besoin"
'''
def appNecessiteuxBesoinsNouveau(request: HttpRequest) -> HttpResponse:
    context = getContextNecessiteux(request)

    if context is None:
        return HttpResponse('404')
    
    context['page_active'] = 'besoins'

    # vider les anciens messages
    storage = messages.get_messages(request)
    for message in storage:
        print(message)
    storage.used = True

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # Traitement pour le formulaire Besoin Financier
        if form_type == settings.BESOIN_FINANCIER:
            formBesoinFinancier = formBesoinFinancier(request.POST)
            if formBesoinFinancier.is_valid():
                besoin_financier = formBesoinFinancier.save(commit=False)
                besoin_financier.necessiteux = context['utilisateur']
                besoin_financier.statut = settings.STATUT_BESOIN_EN_ATTENTE
                besoin_financier.type = settings.BESOIN_FINANCIER
                besoin_financier.save()
                messages.success(request, 'Votre besoin financier a été soumis avec succès et est en attente de validation.')
                return redirect('Necessiteux:appNecessiteuxBesoinsNouveau')
            else:
                messages.error(request, 'Il y a eu une erreur dans le formulaire. Veuillez corriger les erreurs ci-dessous.')
                render(request, 'Necessiteux/app/nouveauBesoin.html', context)
                
        # Traitement pour le formulaire Besoin Matériel
        elif form_type == settings.BESOIN_MATERIEL:
            formBesoinMateriel = BesoinMaterielForm(request.POST)
            if formBesoinMateriel.is_valid():
                besoin_materiel = formBesoinMateriel.save(commit=False)
                besoin_materiel.necessiteux = context['utilisateur']
                besoin_materiel.statut = settings.STATUT_BESOIN_EN_ATTENTE
                besoin_materiel.type = settings.BESOIN_MATERIEL
                besoin_materiel.save()
                messages.success(request, 'Votre besoin matériel a été soumis avec succès et est en attente de validation.')
                return redirect('Necessiteux:appNecessiteuxBesoinsNouveau')
            else:
                messages.error(request, 'Il y a eu une erreur dans le formulaire. Veuillez corriger les erreurs ci-dessous.')
                render(request, 'Necessiteux/app/nouveauBesoin.html', context)
            
        # Traitement pour le formulaire Besoin de Bénévolat
        elif form_type == settings.BESOIN_BENEVOLAT:
            formBesoinBenevolat = BesoinDeBenevolesForm(request.POST)
            if formBesoinBenevolat.is_valid():
                besoin_benevoles = formBesoinBenevolat.save(commit=False)
                besoin_benevoles.necessiteux = context['utilisateur']
                besoin_benevoles.statut = settings.STATUT_BESOIN_EN_ATTENTE
                besoin_benevoles.type = settings.BESOIN_BENEVOLAT
                besoin_benevoles.save()
                messages.success(request, 'Votre besoin de bénévoles a été soumis avec succès et est en attente de validation.')
                return redirect('Necessiteux:appNecessiteuxBesoinsNouveau')
            else:
                messages.error(request, 'Il y a eu une erreur dans le formulaire. Veuillez corriger les erreurs ci-dessous.')
                render(request, 'Necessiteux/app/nouveauBesoin.html', context)
    else:
        formBesoinFinancier = BesoinFinancierForm()
        formBesoinMateriel = BesoinMaterielForm()
        formBesoinBenevolat = BesoinDeBenevolesForm()
        
        context['formBesoinFinancier'] = formBesoinFinancier
        context['formBesoinMateriel'] = formBesoinMateriel
        context['formBesoinBenevolat'] = formBesoinBenevolat

        return render(request, 'Necessiteux/app/nouveauBesoin.html', context)
    

#cette vue permet de creer un besoin materiel
def creer_besoin_materiel(request):
    if request.method == 'POST':
        form = BesoinMaterielForm(request.POST, request.FILES)
        if form.is_valid():
            besoin_materiel = form.save(commit=False)
            besoin_materiel.statut = settings.STATUT_BESOIN_EN_ATTENTE
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
            besoin_financier.statut = settings.STATUT_BESOIN_EN_ATTENTE
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
    besoins = BesoinMateriel.objects.filter(statut=settings.STATUT_BESOIN_EN_ATTENTE)
    if not besoins:
        messages.info(request, 'Il n\'y a pas de besoins matériels en attente.')
    return render(request, 'website_part/besoins_en_attente.html', {'besoins': besoins})

#cette vue permet d'envoyer un besoin de benevolat
def creer_besoin_benevoles(request):
    if request.method == 'POST':
        form = BesoinDeBenevolesForm(request.POST)
        if form.is_valid():
            besoin_benevoles = form.save(commit=False)
            besoin_benevoles.statut = settings.STATUT_BESOIN_EN_ATTENTE
            besoin_benevoles.type = 'Bénévoles'
            besoin_benevoles.save()
            messages.success(request, 'Votre besoin de bénévoles a été soumis avec succès et est en attente de validation.')
            return redirect('website_part:besoinBenevoles_page')
        else:
            messages.error(request, 'Il y a eu une erreur dans le formulaire. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = BesoinDeBenevolesForm()
    return render(request, 'website_part/besoinBenevoles.html', {'form': form})
