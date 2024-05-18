from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'comptes'

urlpatterns = [
    path('login/', register, name = 'login_page')
]
