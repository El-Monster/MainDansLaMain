"""from django.contrib import admin
from .models import NecessiteuxPersonne, NecessiteuxOrganisation

class NecessiteuxPersonneAdmin(admin.ModelAdmin):
    list_display = ('type_necessiteux', 'prenom', 'genre', 'date_naissance', 'user')
    search_fields = ('prenom', 'user__email')
    list_filter = ('type_necessiteux', 'genre')

admin.site.register(NecessiteuxPersonne, NecessiteuxPersonneAdmin)

class NecessiteuxOrganisationAdmin(admin.ModelAdmin):
    list_display = ('type_necessiteux', 'numero_matd', 'agrement_maspfe', 'statut_juridique', 'date_creation', 'user')
    search_fields = ('numero_matd', 'agrement_maspfe', 'user__email')
    list_filter = ('type_necessiteux', 'statut_juridique')

admin.site.register(NecessiteuxOrganisation, NecessiteuxOrganisationAdmin)
"""