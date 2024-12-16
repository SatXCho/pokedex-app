from django.contrib import admin
from .models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'type1', 'type2')
    list_filter = ('type1', 'type2')
    search_fields = ('name', 'number')
    ordering = ('number',)