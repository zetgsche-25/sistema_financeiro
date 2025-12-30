from django.contrib import admin
from .models import Lancamento

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'tipo', 'data')
    list_filter = ('tipo',)
    search_fields = ('descricao',)
