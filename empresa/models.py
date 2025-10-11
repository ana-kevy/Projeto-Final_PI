from django.db import models

class Empresa(models.Model):
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    area_atuacao = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    senha = models.CharField(max_length=128, blank=True, null=True)  # não use como autenticação

    def __str__(self):
        return self.razao_social
