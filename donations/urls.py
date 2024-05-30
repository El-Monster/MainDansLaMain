from django.urls import path
from .views import *

app_name="donations"

urlpatterns = [
    # partie siteweb
    path('creation-compte/donateurPersonne/', donateurPersonne, name='donateurPersonne_compte'),
    path('creation-compte/donateurOrganisation/', donateurOrganisation, name='donateurOrganisation_compte'),
    path('creation-compte/donateurEntreprise/', donateurEntreprise, name='donateurEntreprise_compte'),
    # partie application
    path('faire_donation_materielle/<int:besoin_id>/', faire_donation_materielle, name='faire_donation_materielle'),
    path('app/tableauBord/', donateurTableauBord, name = 'donateurTableauBord'),
]
    
