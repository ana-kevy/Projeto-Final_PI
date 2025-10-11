from django.shortcuts import render, get_object_or_404
from .models import Empresa

# Lista todas as empresas
def listar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa/listar_empresas.html', {'empresas': empresas})

# Detalhes de uma empresa específica
def detalhes_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    return render(request, 'empresa/detalhes_empresa.html', {'empresa': empresa})
