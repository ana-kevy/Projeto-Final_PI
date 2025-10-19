class UsuarioAdaptado(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    curriculo = models.FileField(upload_to='curriculos/', blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    link_portfolio = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True)
    is_candidato = models.BooleanField(default=False)
    is_empresa = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def is_gerente(self):
        return self.groups.filter(name='GERENTE').exists()

    def is_empresa(self):
        return self.groups.filter(name='EMPRESA').exists()

    def is_candidato(self):
        return self.groups.filter(name='CANDIDATO').exists()

