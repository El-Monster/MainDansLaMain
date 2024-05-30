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
from django.contrib import admin
from .models import DonationMaterielle
from django.utils.safestring import mark_safe
class DonationMaterielleAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'quantite', 'description', 'date_reception', 'statut','nom_donateur','afficher_image')
    list_filter = ('statut',)
    search_fields = ('categorie', 'description')
    def afficher_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')

    def nom_donateur(self, obj):
        return obj.donateur.nom  # Supposant que le donateur possède un champ nom_complet

    nom_donateur.short_description = "Donateur" 
admin.site.register(DonationMaterielle, DonationMaterielleAdmin)
