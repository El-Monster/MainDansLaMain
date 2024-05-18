from django.urls import path
from .views import *

app_name = 'Necessiteux'

urlpatterns = [
    path('necessiteuxPersonne/', necessiteuxPersonne, name='necessiteuxPersonne_compte'),
    path('necessiteuxOrganisation/', necessiteuxOrganisation, name='necessiteuxOrganisation_compte')
]
