from django.urls import path
from .views import *

app_name="donations"

urlpatterns = [
    path('creation-compte/donateurPersonne/', donateurPersonne, name='donateurPersonne_compte'),
    path('creation-compte/donateurOrganisation/',donateurOrganisation, name='donateurOrganisation_compte'),
    path('creation-compte/donateurEntreprise/', donateurEntreprise, name='donateurEntreprise_compte'),
    path('creation-compte/donateurCompte/', donateurcompte, name='donateur_compte')
    ]
    
