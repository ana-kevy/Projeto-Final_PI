from django.db import models
from empresa.models import Empresa
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Vaga(models.Model):
    titulo = models.CharField(max_length=255)
    requisitos = models.TextField(blank=True, null=True)
    local = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)  # Presencial / Remoto
    remuneracao = models.CharField(max_length=100, blank=True, null=True)
    carga_horaria = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='vagas')

    def __str__(self):
        return f"{self.titulo} - {self.empresa}"


class Candidatura(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_analise', 'Em análise'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    ]
    candidato = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidaturas')
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='candidaturas')
    data_candidatura = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        unique_together = ('candidato', 'vaga')

    def __str__(self):
        return f"{self.candidato} -> {self.vaga}"
