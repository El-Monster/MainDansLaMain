from django.contrib import admin
from .models import AgentCollecte
# Register your models here.
class AgentCollecteAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'date_naissance', 'email', 'localisation_geographique')
    search_fields = ('prenom', 'email')
admin.site.register(AgentCollecte, AgentCollecteAdmin)
