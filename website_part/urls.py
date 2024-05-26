from django.urls import path
from . import views
from .views import besoins_en_attente

app_name = 'website_part'

urlpatterns = [
    path('', views.index , name='index'),
    path('apropos/', views.a_propos, name = 'a_propos'),
    path('actions/', views.actions, name = 'nos_actions'),
    # path('besoins/', views.besoins, name = 'envoyer_besoin'),
    path('donations/', views.donations, name = 'faire_donation'),
    path('contactez_nous/', views.contactez_nous, name = 'contactez_nous'),
    path('authentification/', views.se_connecter, name = 'se_connecter'),
    path('besoinMateriel/', views.creer_besoin_materiel, name = 'besoinMateriel_page'),
    path('besoinFinancier/', views.creer_besoin_financier, name = 'besoinFinancier_page'),
    path('besoins-en-attente/', besoins_en_attente, name='besoins_en_attente_page'),
    path('besoins-de-benevole/', views.creer_besoin_benevoles, name='besoinBenevoles_page')
]