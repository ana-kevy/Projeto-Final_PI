from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Mensagem


@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('cpf', 'endereco', 'curriculo', 'habilidades', 'link_portfolio', 'is_admin')}),
    )


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('candidato', 'empresa', 'data_hora')
    search_fields = ('conteudo',)
