from django.contrib import admin
from .models import UtilisateurPersonnalise

class UtilisateurPersonnaliseAdmin(admin.ModelAdmin):
    list_display = ('email', 'nom', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'nom')

admin.site.register(UtilisateurPersonnalise, UtilisateurPersonnaliseAdmin)