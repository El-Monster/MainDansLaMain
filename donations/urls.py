from django.urls import path
from .views import *

urlpatterns = [
    path('don/', index, name='index_page')
]
