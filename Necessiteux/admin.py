from django.contrib import admin
from donations.models import DonateurPersonne

class DonateurPersonneAdmin(admin.ModelAdmin):
    pass  # Vous pouvez personnaliser l'affichage et le comportement de l'administration ici si nécessaire

admin.site.register(DonateurPersonne, DonateurPersonneAdmin)
