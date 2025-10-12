from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    curriculo = models.FileField(upload_to='curriculos/', blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    link_portfolio = models.URLField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name() or self.username
