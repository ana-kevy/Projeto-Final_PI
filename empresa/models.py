from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empresa')
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
