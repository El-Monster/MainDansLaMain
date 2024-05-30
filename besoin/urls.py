from django.urls import path
from .views import besoins_en_cours,faire_don
app_name="besoin"
urlpatterns = [
    # Ajoutez l'URL pour la vue besoins_en_cours
    path('besoins-en-cours/', besoins_en_cours, name='besoins_en_cours'),
    path('faire_don/<int:besoin_id>/', faire_don, name='faire_don'),
]
