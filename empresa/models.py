from django.db import models

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    area_atuacao = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.razao_social
