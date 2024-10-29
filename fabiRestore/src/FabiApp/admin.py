from django.contrib import admin

from .models import Meuble

@admin.register(Meuble)
class MeubleAdmin(admin.ModelAdmin):

    list_display = ('titre','statut','prix')
    list_filter = ('titre','statut','prix','date')
    search_fields = ('titre',)
    list_per_page = 8
