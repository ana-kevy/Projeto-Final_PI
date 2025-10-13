from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Empresa
from .forms import EmpresaForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa/listar.html', {'empresas': empresas})

@login_required
def criar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('listar_empresas')
        else:
            messages.error(request, 'Erro ao cadastrar empresa.')
    else:
        form = EmpresaForm()
    return render(request, 'empresa/form.html', {'form': form, 'titulo': 'Cadastrar Empresa'})

@login_required
def editar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa atualizada com sucesso!')
            return redirect('listar_empresas')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresa/form.html', {'form': form, 'titulo': 'Editar Empresa'})

@login_required
def deletar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        messages.success(request, 'Empresa excluída com sucesso!')
        return redirect('listar_empresas')
    return render(request, 'empresa/confirmar_delete.html', {'empresa': empresa})
