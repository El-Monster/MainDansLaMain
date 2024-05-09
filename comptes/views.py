from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def creation_compte(request):
    return render(request, 'comptes/creation_compte.html')
def compte_necessiteux(request):
    return render(request, 'comptes/compte_necessiteux.html')
def compte_donateur(request):
    return render(request, 'comptes/compte_donateur.html')
def compte_benevole(request):
    return render(request, 'comptes/compte_benevole.html')
