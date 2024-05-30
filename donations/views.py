from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.hashers import make_password
from Necessiteux.models import Besoin
from donations.models import DonateurEntreprise, DonateurOrganisation, DonateurPersonne, Visiteur

from .forms import DonateurPersonneForm, DonateurOrganisationForm, DonateurEntrepriseForm, DonationMaterielleForm, VisiteurForm

from django.contrib.auth import get_user_model, logout
from django.contrib import messages

# Create your views here.

#creation de la vue pour la page
def donateurPersonne(request: HttpRequest):
    if request.method == 'POST':
        form = DonateurPersonneForm(request.POST,request.FILES)
        if form.is_valid() :
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User = get_user_model()
            # Vérifier si le compte email existe déjà dans la base de données
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email a déjà un compte.')
                return render(request, 'donations/donateurPersonne.html', {'form': form})
            
            # Vérifier si le mot de passe est sécurisé
            if not is_secure_password(password):
                messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
                return render(request, 'donations/donateurPersonne.html', {'form': form})
            
            hashed_password = make_password(password)
            user = form.save(commit=False)
            user.password = hashed_password
            
            # Attribution du role
            user.role = settings.DONATEUR
            
            donateur = form.save(commit=False)
            
            # Attribution du type
            donateur.type_donateur = settings.PERSONNE
            donateur.user = user
            donateur.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:se_connecter')
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
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email a déjà un compte.')
                return render(request, 'donations/donateurEntreprise.html', {'form': form})
            
            # Vérifier si le mot de passe est sécurisé
            if not is_secure_password(password):
                messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
                return render(request, 'donations/donateurEntreprise.html', {'form': form})
            
            hashed_password = make_password(password)
            user = form.save(commit=False)
            user.password = hashed_password
            
            # Attribution du role
            user.role = settings.DONATEUR

            donateur = form.save(commit=False)
            
            # Attribution du type
            donateur.type_donateur = settings.ENTREPRISE
            donateur.user = user
            donateur.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:se_connecter')
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
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email a déjà un compte.')
                return render(request, 'donations/donateurOrganisation.html', {'form': form})
            
            if not is_secure_password(password):
                messages.error(request, 'Le mot de passe ne correspond pas aux critères de sécurité.')
                return render(request, 'donations/donateurOrganisation.html', {'form': form})
            
            hashed_password = make_password(password)
            user = form.save(commit=False)
            user.password = hashed_password
            
            # Attribution du role
            user.role = settings.DONATEUR
            
            donateur = form.save(commit=False)
            
            #attribution de type
            donateur.type_donateur = settings.ORGANISATION

            donateur.user = user
            donateur.save()
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('website_part:se_connecter')
        else:
            # Si le formulaire est invalide, renvoyer le formulaire avec les erreurs
            return render(request, 'donations/donateurOrganisation.html', {'form': form})
    else:
        form = DonateurOrganisationForm()
        return render(request, 'donations/donateurOrganisation.html', {'form': form})


# La vue qui génère le 'tableauBord' du donateur 
def donateurTableauBord(request: HttpRequest) -> HttpResponse:
    context = request.session.get('context', {})

    # Récupérer l'objet DonateurPersonne si l'ID est présent dans le contexte
    if 'utilisateur_id' in context:
        utilisateur_id = context['utilisateur_id']
        context['utilisateur'] = DonateurPersonne.objects.get(id=utilisateur_id)

    return render(request, 'donations/app/tableauBord.html', context)


def get_donateur(user):
    try:
        if hasattr(user, 'donateurpersonne'):
            return user.donateurpersonne
        elif hasattr(user, 'donateurentreprise'):
            return user.donateurentreprise
        elif hasattr(user, 'donateurorganisation'):
            return user.donateurorganisation
        elif hasattr(user, 'visiteur'):
            return user.visiteur
    except (DonateurPersonne.DoesNotExist, DonateurEntreprise.DoesNotExist, DonateurOrganisation.DoesNotExist, Visiteur.DoesNotExist):
        return None
    return None



def faire_donation_materielle(request, besoin_id = None):
    besoin = get_object_or_404(Besoin, id=besoin_id)
    
    print(f"Identifiant du besoin est {besoin}")
    if request.user.is_authenticated:
        donateur = get_donateur(request.user)
        if not donateur:
            # Gérer le cas où l'utilisateur connecté n'est pas un donateur
            logout(request)
            messages.error(request, "Vous devez être un donateur pour faire un don.")
            return redirect('website_part:se_connecter')  # Remplacez 'profile_creation_url' par l'URL appropriée

        if request.method == 'POST':
            donation_form = DonationMaterielleForm(request.POST, request.FILES)
            if donation_form.is_valid():
                donation = donation_form.save(commit=False)
                donation.donateur = donateur
                donation.besoin = besoin  # Associez la donation au besoin
                donation.save()
                messages.success(request, "Votre don a été enregistré avec succès.")
                return redirect('success_url')  # Remplacez 'success_url' par l'URL de redirection souhaitée
        else:
            donation_form = DonationMaterielleForm()
        return render(request, 'website_part/faire_donation.html', {'donation_form': donation_form, 'besoin': besoin})
    else:
        # L'utilisateur n'est pas connecté
        if request.method == 'POST':
            visiteur_form = VisiteurForm(request.POST)
            print(visiteur_form.errors)
            donation_form = DonationMaterielleForm(request.POST, request.FILES)
            print(donation_form.errors)
            if visiteur_form.is_valid() and donation_form.is_valid():
                visiteur = visiteur_form.save(commit=False)
                visiteur.save()
                donation = donation_form.save(commit=False)
                
                #donation.donateur.type="Anonyme"
                donation.donateur = visiteur # Associez la donation au visiteur créé
                donation.besoin = besoin  # Associez la donation au besoin
                donation.save()
                messages.success(request, "Votre don a été enregistré avec succès.")
                return redirect('donations:faire_donation_materielle')  # Remplacez 'success_url' par l'URL de redirection souhaitée
        else:
            visiteur_form = VisiteurForm()
            donation_form = DonationMaterielleForm()

        return render(request, 'website_part/faire_donation.html', {'visiteur_form': visiteur_form, 'donation_form': donation_form, 'besoin': besoin})