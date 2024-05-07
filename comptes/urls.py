from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'comptes'

urlpatterns = [
    path('login/',creation_compte,name ='creation_compte'),
    path('necessite/',compte_necessiteux,name='compte_necessiteux'),
    path('donateur/',compte_donateur,name='compte_donateur'),
    path('benevole/',compte_benevole,name='compte_benevole')
]
