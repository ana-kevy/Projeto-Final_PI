from django.db import models

class Usuario(models.Model):
    id_candidato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    curriculo = models.FileField(upload_to='curriculos/', null=True, blank=True)
    habilidades = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    link_portfolio = models.URLField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

