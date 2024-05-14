from django.contrib import admin
from .models import DonateurEntreprise

class DonateurEntrepriseAdmin(admin.ModelAdmin):
    pass  # Vous pouvez personnaliser l'affichage et le comportement de l'administration ici si nécessaire

admin.site.register(DonateurEntreprise, DonateurEntrepriseAdmin)
from django.contrib import admin

# Register your models here.
