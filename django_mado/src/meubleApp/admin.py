from django.contrib import admin
from meubleApp.models import Auteur, Meuble

@admin.register(Meuble)
class MeubleAdmin(admin.ModelAdmin):

    # Pour faire des sous parties dans l'affichage d'un objet Meuble sur la page admin
    fieldsets =[
        ('Vente', {'fields': ['titre', 'couleur', 'prix']}),
        ('Réalisation', {'fields': ['date', 'auteur']})

    ]

    list_display = ('titre','auteur',)
    list_filter = ('auteur',)
    search_fields = ('titre',)
    list_per_page = 8
    # inlines=(UserInLine,)

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('nom','age',)
    search_fields = ('nom',)

# admin.site.register(Auteur, AuteurAdmin)
# admin.site.register(Meuble, MeubleAdmin)

