from django.contrib import admin
from .models import Besoin, BesoinMateriel, BesoinFinancier,BesoinDeBenevoles

# Classe admin pour le modèle Besoin
class BesoinAdmin(admin.ModelAdmin):
    list_display = ['titre', 'degre_urgence', 'date_creation', 'statut', 'envoyeur', 'type_besoin']
    search_fields = ['titre', 'degre_urgence']
    list_filter = ['degre_urgence', 'statut']
    date_hierarchy = 'date_creation'
    actions = ['valider_besoins']
    list_per_page = 5
    def valider_besoins(self, request, queryset):
        queryset.update(statut='En cours')
    valider_besoins.short_description = "Valider les besoins sélectionnés"
    def envoyeur(self, obj):
        return obj.necessiteux.email
    envoyeur.short_description = 'Envoyé par'

    def type_besoin(self, obj):
        return obj.__class__.__name__
    type_besoin.short_description = 'Type de Besoin'

# Classes inline pour les modèles associés à Besoin
class BesoinMaterielInline(admin.StackedInline):
    model = BesoinMateriel

class BesoinFinancierInline(admin.StackedInline):
    model = BesoinFinancier

# Classe admin pour le modèle BesoinMateriel
@admin.register(BesoinMateriel)
class BesoinMaterielAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'quantite', 'statut', 'description', 'necessiteux_name']
    search_fields = ['titre', 'categorie']
    list_filter = ['categorie']
    actions = ['valider_besoins']
    list_per_page = 5
    def necessiteux_name(self, obj):
        return obj.necessiteux.email
    necessiteux_name.short_description = 'Envoyé par'

    def valider_besoins(self, request, queryset):
        queryset.update(statut='En cours')
    valider_besoins.short_description = "Valider les besoins sélectionnés"

    class Meta:
        verbose_name_plural = "Sélectionner le besoin à changer"

# Classe admin pour le modèle BesoinFinancier
@admin.register(BesoinFinancier)
class BesoinFinancierAdmin(admin.ModelAdmin):
    list_display = ['titre', 'montant_souhaite', 'montant_collecte', 'necessiteux_name', 'statut']
    search_fields = ['titre']
    list_filter = ['montant_souhaite']
    actions = ['valider_besoins']
    list_per_page = 5
    def necessiteux_name(self, obj):
        return obj.necessiteux.email
    necessiteux_name.short_description = 'Envoyé par'

    def valider_besoins(self, request, queryset):
        queryset.update(statut='En cours')
    valider_besoins.short_description = "Valider les besoins sélectionnés"


@admin.register(BesoinDeBenevoles)
class BesoinDeBenevolesAdmin(admin.ModelAdmin):
    list_display = ['titre', 'description', 'degre_urgence', 'duree', 'nombre_de_benevoles', 'competences_demandees', 'statut', 'necessiteux']
    search_fields = ['titre', 'description', 'competences_demandees', 'necessiteux__email']
    list_filter = ['degre_urgence', 'statut', 'duree', 'nombre_de_benevoles']
    list_per_page = 5
    def necessiteux_name(self, obj):
        return obj.necessiteux.email
    necessiteux_name.short_description = 'Envoyé par'

    actions = ['valider_besoins']

    def valider_besoins(self, request, queryset):
        queryset.update(statut='En cours')
    valider_besoins.short_description = "Valider les besoins sélectionnés"

# Enregistrement du modèle Besoin avec sa classe admin
admin.site.register(Besoin, BesoinAdmin)
