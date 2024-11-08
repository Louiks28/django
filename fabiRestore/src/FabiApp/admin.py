from django.contrib import admin

from .models import Meuble, Photo

@admin.register(Meuble)
class MeubleAdmin(admin.ModelAdmin):

    list_display = ('titre','statut','prix', 'categorie')
    list_filter = ('titre','statut','prix','date')
    search_fields = ('titre',)
    list_per_page = 8

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ('meuble_titre','image')
    # list_filter = ('titre','statut','prix','date')
    # search_fields = ('titre',)
    list_per_page = 8

    def meuble_titre(self, obj):
        return obj.meuble.titre
    meuble_titre.short_description = 'Meuble'
