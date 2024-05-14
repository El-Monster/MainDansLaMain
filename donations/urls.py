from django.urls import path
from .views import *

# pour afficher un template d'une autre app on inclus
from django.views.generic import TemplateView

urlpatterns = [
    path('don/', index, name='index_page'),
    path('user/', user, name = 'user')
]
