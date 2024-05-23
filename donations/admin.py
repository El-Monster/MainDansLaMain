"""from django.contrib import admin
from .models import DonateurPersonne, DonateurEntreprise, DonateurOrganisation

class DonateurPersonneAdmin(admin.ModelAdmin):
    list_display = ('type_donateur', 'prenom', 'genre', 'date_naissance', 'user')
    search_fields = ('prenom', 'user__email')
    list_filter = ('type_donateur', 'genre')

admin.site.register(DonateurPersonne, DonateurPersonneAdmin)

class DonateurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ('type_donateur', 'numero_fiscal', 'statut_juridique', 'date_creation', 'user')
    search_fields = ('numero_fiscal', 'user__email')
    list_filter = ('type_donateur', 'statut_juridique')

admin.site.register(DonateurEntreprise, DonateurEntrepriseAdmin)

class DonateurOrganisationAdmin(admin.ModelAdmin):
    list_display = ('type_donateur', 'numero_MATD', 'statut_juridique', 'date_creation', 'user')
    search_fields = ('numero_MATD', 'user__email')
    list_filter = ('type_donateur', 'statut_juridique')

admin.site.register(DonateurOrganisation, DonateurOrganisationAdmin)
"""