from django.contrib import admin
from .models import Vaga, Mensagem

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'salario', 'ativo', 'data_publicacao')
    search_fields = ('titulo', 'empresa__nome')
    list_filter = ('ativo', 'empresa')
    ordering = ('-data_publicacao',)

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('vaga', 'empresa', 'candidato', 'data_envio')
    search_fields = ('vaga__titulo', 'empresa__nome', 'candidato__username')
    list_filter = ('data_envio', 'empresa')
