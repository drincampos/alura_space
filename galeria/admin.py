from django.contrib import admin
from .models import Fotografia


class ListaFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_filter = ('categoria',)
    list_editable = ('publicada',)

admin.site.register(Fotografia, ListaFotografias)