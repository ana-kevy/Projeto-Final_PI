from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Empresa
from .forms import EmpresaForm

# Apenas usuários do tipo empresa podem acessar
def is_empresa(user):
    return user.is_authenticated and getattr(user, "is_empresa", False)


@login_required
@user_passes_test(is_empresa)
def listar_empresas(request):
    # Exibe apenas empresas do usuário logado
    empresas = Empresa.objects.filter(usuario=request.user)
    return render(request, 'empresa/listar.html', {'empresas': empresas})


@login_required
@user_passes_test(is_empresa)
def criar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.usuario = request.user  # 🔗 Vincula ao usuário logado
            empresa.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('empresa:listar_empresas')
        else:
            messages.error(request, 'Erro ao cadastrar empresa.')
    else:
        form = EmpresaForm()
    return render(request, 'empresa/form.html', {'form': form, 'titulo': 'Cadastrar Empresa'})


@login_required
@user_passes_test(is_empresa)
def editar_empresa(request, pk):
    # Garante que só edite a própria empresa
    empresa = get_object_or_404(Empresa, pk=pk, usuario=request.user)
    form = EmpresaForm(request.POST or None, instance=empresa)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Empresa atualizada com sucesso!')
        return redirect('empresa:listar_empresas')
    return render(request, 'empresa/form.html', {'form': form, 'titulo': 'Editar Empresa'})


@login_required
@user_passes_test(is_empresa)
def deletar_empresa(request, pk):
    # Só deleta se for o dono
    empresa = get_object_or_404(Empresa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        empresa.delete()
        messages.success(request, 'Empresa excluída com sucesso!')
        return redirect('empresa:listar_empresas')
    return render(request, 'empresa/confirmar_delete.html', {'empresa': empresa})
