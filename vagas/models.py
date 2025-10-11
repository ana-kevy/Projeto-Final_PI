from django.db import models
from empresa.models import Empresa
from usuario.models import Usuario


class Vaga(models.Model):
    id_vaga = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    requisitos = models.TextField()
    local = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2)
    carga_horaria = models.CharField(max_length=50)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='vagas')

    def __str__(self):
        return self.titulo


class Candidatura(models.Model):
    id_candidatura = models.AutoField(primary_key=True)
    data_candidatura = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pendente')
    id_candidato = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='candidaturas')
    id_vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='candidaturas')

    def __str__(self):
        return f'{self.id_candidato.nome} - {self.id_vaga.titulo}'


class Mensagem(models.Model):
    id_mensagem = models.AutoField(primary_key=True)
    conteudo = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    id_candidato = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens')
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='mensagens')

    def __str__(self):
        return f'Mensagem de {self.id_candidato.nome} para {self.id_empresa.razao_social}'

