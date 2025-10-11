from django.db import models
from django.contrib.auth.models import AbstractUser
from empresa.models import Empresa

class Usuario(AbstractUser):
    # herdando username, password, email, first_name, last_name, is_staff, is_active, ...
    cpf = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    curriculo = models.FileField(upload_to='curriculos/', blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    link_portfolio = models.URLField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)  # seu diagrama tinha is_admin

    def __str__(self):
        return self.get_full_name() or self.username
    
class Mensagem(models.Model):
    conteudo = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    candidato = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='mensagens')

    def __str__(self):
        return f"Mensagem de {self.candidato} para {self.empresa}"
