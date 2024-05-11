from django.shortcuts import render,redirect
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.template import loader
from .forms import UtilisateurForm

# Create your views here.
"""def creation_compte(request):
    return render(request, 'comptes/creation_compte.html')"""
def creation_compte(request):
    # Vérifier si le formulaire a été soumis
    if request.method == 'POST':
        # Créer une instance de UtilisateurForm avec les données soumises
        form = UtilisateurForm(request.POST, request.FILES)
        # Vérifier si le formulaire est valide
        if form.is_valid():
            # Sauvegarder les données de l'utilisateur dans la base de données
            form.save()
            # Rediriger vers une page de succès ou une autre vue
            return redirect('comptes:compte_donateur')
    else:
        # Si la méthode de requête est GET, créer une instance vide de UtilisateurForm
        form = UtilisateurForm()
        
    
    # Rendre le template avec le formulaire
    return render(request, 'comptes/creation_compte.html', {'form': form})  
def compte_necessiteux(request):
    return render(request, 'comptes/compte_necessiteux.html')
def compte_donateur(request):
    return render(request, 'comptes/compte_donateur.html')
def compte_benevole(request):
    return render(request, 'comptes/compte_benevole.html')
