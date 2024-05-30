from django.urls import path
from .views import *

app_name = 'Necessiteux'

urlpatterns = [
    # partie siteweb
    path('necessiteuxPersonne/', necessiteuxPersonne, name='necessiteuxPersonne_compte'),
    path('necessiteuxOrganisation/', necessiteuxOrganisation, name='necessiteuxOrganisation_compte'),
    # partie application
    path('app/necessiteux/tableauBord/', appNecessiteuxTableauBord, name = 'appNecessiteuxTableauBord'),
    path('app/necessiteux/besoins/', appNecessiteuxBesoins, name = 'appNecessiteuxBesoins'),
    path('app/necessiteux/besoins/nouveauBesoin', appNecessiteuxBesoinsNouveau, name = 'appNecessiteuxBesoinsNouveau'),
]
