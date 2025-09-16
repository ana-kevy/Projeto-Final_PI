from django.db import models

class Candidato(models.Model):
    id_candidato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    formacao = models.TextField(blank=True, null=True)
    experiencias = models.TextField(blank=True, null=True)
    cursos = models.TextField(blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    link_portfolio = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # senha criptografada

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    area_atuacao = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.razao_social


class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    id_vaga = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    requisitos = models.TextField()
    local = models.CharField(max_length=150)
    tipo = models.CharField(max_length=50, choices=[('emprego','Emprego'), ('estagio','Estágio'), ('bolsa','Bolsa')])
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    carga_horaria = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="vagas")

    def __str__(self):
        return f"{self.titulo} - {self.empresa.razao_social}"


class Candidatura(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('analise', 'Em análise'),
        ('selecionado', 'Selecionado'),
        ('rejeitado', 'Rejeitado'),
    ]
    id_candidatura = models.AutoField(primary_key=True)
    data_candidatura = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name="candidaturas")
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name="candidaturas")

    def __str__(self):
        return f"{self.candidato.nome} -> {self.vaga.titulo}"

class Mensagem(models.Model):
    id_mensagem = models.AutoField(primary_key=True)
    conteudo = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name="mensagens")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="mensagens")

    def __str__(self):
        return f"Mensagem de {self.candidato.nome} para {self.empresa.razao_social}"


class Notificacao(models.Model):
    id_notificacao = models.AutoField(primary_key=True)
    descricao = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name="notificacoes")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="notificacoes")

    def __str__(self):
        return f"Notificação para {self.candidato.nome}"

class Relatorio(models.Model):
    id_relatorio = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_geracao = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name="relatorios")

    def __str__(self):
        return f"Relatório {self.tipo} - {self.admin.nome}"
