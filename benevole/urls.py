from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'benevole'

urlpatterns = [
    path('benevolePersonne/', compte_benevole, name ='benevolePersonne_compte'),
   
]