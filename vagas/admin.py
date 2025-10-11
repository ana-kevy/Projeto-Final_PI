from django.contrib import admin
from .models import Vaga, Candidatura

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'local', 'tipo', 'remuneracao')

@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('candidato', 'vaga', 'data_candidatura', 'status')
