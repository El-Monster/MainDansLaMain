from django.shortcuts import render,redirect
from .necessiteuxPersonneForm import NecessiteuxPersonneForm
from .necessiteuxOrganisationForm import NecessiteuxOrganisationForm
# Create your views here.
#creation de la vue pour la page de don
def necessiteuxPersonne(request):
    if request.method == 'POST':
        form = NecessiteuxPersonneForm(request.POST)
        if form.is_valid():
            necessiteux_personne = form.save()
            # Redirection vers une autre vue ou une autre URL après avoir enregistré le nécessiteux
            return redirect('')
    else:
        form = NecessiteuxPersonneForm()
    return render(request, 'Necessiteux/NecessiteuxPersonne.html', {'form': form})

def necessiteuxOrganisation(request):
    if request.method == 'POST':
        form = NecessiteuxOrganisationForm(request.POST)
        if form.is_valid():
            necessiteux_organisation = form.save()
            # Redirection vers une autre vue ou une autre URL après avoir enregistré le nécessiteux
            return redirect('nom_de_votre_vue_ou_url')
    else:
        form = NecessiteuxOrganisationForm()
    return render(request, 'Necessiteux/Necessiteuxorganisation.html', {'form': form})