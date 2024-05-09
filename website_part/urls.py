from django.urls import path
from . import views

app_name = 'website_part'

urlpatterns = [
    path('', views.index , name='index'),
    path('apropos/', views.a_propos, name = 'a_propos'),
    path('actions/', views.actions, name = 'nos_actions'),
    path('besoins/', views.besoins, name = 'envoyer_besoin'),
    path('donations/', views.donations, name = 'faire_donation'),
    path('contactez_nous/', views.contactez_nous, name = 'contactez_nous'),
    path('authentification/', views.se_connecter, name = 'se_connecter'),
]