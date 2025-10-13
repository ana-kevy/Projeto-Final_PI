from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'endereco')
    search_fields = ('nome', 'cnpj')
    list_filter = ('endereco',)
