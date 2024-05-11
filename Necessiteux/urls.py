from django.urls import path
from .views import *

urlpatterns = [
    path('necessiteuxPersonne/', necessiteuxPersonne, name='necessiteuxPersonne_Page'),
    path('necessiteuxOrganisation/', necessiteuxOrganisation, name='necessiteuxorganisation_Page')
]
