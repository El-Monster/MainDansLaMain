from django.urls import path
from .views import *
app_name="donations"
urlpatterns = [
    path('donateurPersonne/', donateurPersonne, name='donateurPersonne_compte'),
    path('donateurorganisation/',donateurOrganisation, name='donateurOrganisation_compte'),
    path('donateurentreprise/', donateurEntreprise, name='donateurEntreprise_compte'),
    path('donateurcompte/', donateurcompte, name='donateur_compte')
    ]
    
