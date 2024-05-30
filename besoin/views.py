from django.shortcuts import render
from website_part.models import Besoin, BesoinMateriel, BesoinFinancier, BesoinDeBenevoles
from django.contrib import messages
from benevole.visiteurForm import VisiteurForm
from django.shortcuts import render, redirect, get_object_or_404
from donations.donation import DonationMaterielleForm
from donations.models import Besoin, Visiteur, DonateurPersonne, DonateurEntreprise, DonateurOrganisation
from django.contrib.auth import logout
def besoins_en_cours(request):
    # Récupérer tous les besoins en cours
    besoins = Besoin.objects.filter(statut='En cours')

    # Récupérer les besoins matériels en cours
    besoins_materiels = BesoinMateriel.objects.filter(statut='En cours')

    # Récupérer les besoins financiers en cours
    besoins_financiers = BesoinFinancier.objects.filter(statut='En cours')

    # Récupérer les besoins de bénévoles en cours
    besoins_benevoles = BesoinDeBenevoles.objects.filter(statut='En cours')

    # Fusionner toutes les listes de besoins
    tous_les_besoins =  list(besoins_materiels) + list(besoins_financiers) + list(besoins_benevoles)
    print(f" tous les besoins{tous_les_besoins}")

    # Renvoyer les besoins au template
    return render(request, 'besoin/listeBesoin.html', {'tous_les_besoins': tous_les_besoins})



"""def faire_don(request, besoin_id=None):
    besoin = get_object_or_404(Besoin, id=besoin_id)
    print(f"identifaint du besoin est{besoin }")
    if request.user.is_authenticated:
        # L'utilisateur est connecté
        if request.method == 'POST':
            donation_form = DonationMaterielleForm(request.POST, request.FILES)
            if donation_form.is_valid():
                donation = donation_form.save(commit=False)
                donation.donateur = request.user
                donation.besoin = besoin  # Associez la donation au besoin
                donation.save()
                messages.success(request, "Votre don a été enregistré avec succès.")
                return redirect('success_url')  # Remplacez 'success_url' par l'URL de redirection souhaitée
        else:
            donation_form = DonationMaterielleForm()
        return render(request, 'website_part/dons.html', {'donation_form': donation_form, 'besoin': besoin})
    else:
        # L'utilisateur n'est pas connecté
        if request.method == 'POST':
            visiteur_form = VisiteurForm(request.POST)
            print(visiteur_form.errors)
            donation_form = DonationMaterielleForm(request.POST, request.FILES)
            print(DonationMaterielleForm.errors)
            if visiteur_form.is_valid() and donation_form.is_valid():
                visiteur = visiteur_form.save(commit=False)
                # Si le visiteur n'a pas de mot de passe, nous n'appelons pas set_password
                if visiteur.password:
                    visiteur.set_password(visiteur.password)
                visiteur.save()
                donation = donation_form.save(commit=False)
                donation.donateur = visiteur  # Associez la donation au visiteur créé
                donation.besoin = besoin  # Associez la donation au besoin
                donation.save()
                messages.success(request, "Votre don a été enregistré avec succès.")
                return redirect('success_url')  # Remplacez 'success_url' par l'URL de redirection souhaitée
        else:
            visiteur_form = VisiteurForm()
            donation_form = DonationMaterielleForm()

      return render(request, 'website_part/dons.html', {'visiteur_form': visiteur_form, 'donation_form': donation_form, 'besoin': besoin})

"""



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

def faire_don(request, besoin_id=None):
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
        return render(request, 'website_part/dons.html', {'donation_form': donation_form, 'besoin': besoin})
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
                donation.donateur.type="Anonyme"
                donation.donateur = visiteur # Associez la donation au visiteur créé
                donation.besoin = besoin  # Associez la donation au besoin
                donation.save()
                messages.success(request, "Votre don a été enregistré avec succès.")
                return redirect('success_url')  # Remplacez 'success_url' par l'URL de redirection souhaitée
        else:
            visiteur_form = VisiteurForm()
            donation_form = DonationMaterielleForm()

        return render(request, 'website_part/dons.html', {'visiteur_form': visiteur_form, 'donation_form': donation_form, 'besoin': besoin})
