from django.contrib import admin

from django.contrib import admin
from .models import Candidato, Empresa, Administrador, Vaga, Candidatura, Mensagem, Notificacao, Relatorio

admin.site.register(Candidato)
admin.site.register(Empresa)
admin.site.register(Administrador)
admin.site.register(Vaga)
admin.site.register(Candidatura)
admin.site.register(Mensagem)
admin.site.register(Notificacao)
admin.site.register(Relatorio)
