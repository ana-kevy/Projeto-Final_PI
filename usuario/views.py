from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from .models import UsuarioAdaptado
from .forms import UsuarioAdaptadoCreationForm, LoginForm, PerfilForm, UsuarioEditForm, UsuarioFiltroForm


# ========= CADASTRO =========
def cadastrar_usuario(request):
    """Cadastro normal de usuário (empresa ou candidato)"""
    if request.method == 'POST':
        form = UsuarioAdaptadoCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Cadastro de {user.username} realizado com sucesso!')
            return redirect('login')
    else:
        form = UsuarioAdaptadoCreationForm()
    return render(request, 'usuarios/cadastrar.html', {'form': form})


# ========= LOGIN / LOGOUT =========
def login_view(request):
    if request.user.is_authenticated:
        return redirect('listar_vagas')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')

                # Redirecionamento conforme grupo
                if user.is_empresa():
                    return redirect('painel_empresa')
                elif user.is_candidato():
                    return redirect('listar_vagas')
                elif user.is_gerente():
                    return redirect('listar_usuarios')
                return redirect('listar_vagas')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('login')


# ========= PERFIL =========
@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user)
    return render(request, 'usuarios/perfil.html', {'form': form})


# ========= GESTÃO DE USUÁRIOS (somente gerente/admin) =========
@login_required
def listar_usuarios(request):
    if not request.user.is_gerente() and not request.user.is_superuser:
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('listar_vagas')

    usuarios = UsuarioAdaptado.objects.all().order_by('-date_joined')
    filtro_form = UsuarioFiltroForm(request.GET or None)

    if filtro_form.is_valid():
        if filtro_form.cleaned_data.get('username'):
            usuarios = usuarios.filter(username__icontains=filtro_form.cleaned_data['username'])
        if filtro_form.cleaned_data.get('email'):
            usuarios = usuarios.filter(email__icontains=filtro_form.cleaned_data['email'])
        if filtro_form.cleaned_data.get('cpf'):
            usuarios = usuarios.filter(cpf__icontains=filtro_form.cleaned_data['cpf'])

    paginator = Paginator(usuarios, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': page_obj, 'filtro_form': filtro_form})


@login_required
def criar_usuario_admin(request):
    if not request.user.is_gerente() and not request.user.is_superuser:
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('listar_vagas')

    if request.method == 'POST':
        form = UsuarioAdaptadoCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Usuário {user.username} criado com sucesso!')
            return redirect('listar_usuarios')
    else:
        form = UsuarioAdaptadoCreationForm()
    return render(request, 'usuarios/form_usuario.html', {'form': form, 'titulo': 'Criar Novo Usuário'})


@login_required
def editar_usuario_admin(request, pk):
    if not request.user.is_gerente() and not request.user.is_superuser:
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('listar_vagas')

    usuario = get_object_or_404(UsuarioAdaptado, pk=pk)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuário {usuario.username} atualizado com sucesso!')
            return redirect('listar_usuarios')
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'usuarios/form_usuario.html', {'form': form, 'titulo': f'Editar Usuário: {usuario.username}'})


@login_required
def deletar_usuario(request, pk):
    if not request.user.is_gerente() and not request.user.is_superuser:
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('listar_vagas')

    usuario = get_object_or_404(UsuarioAdaptado, pk=pk)
    if usuario == request.user:
        messages.error(request, 'Você não pode deletar seu próprio usuário!')
        return redirect('listar_usuarios')

    if usuario.is_superuser:
        messages.error(request, 'Não é possível deletar um superusuário!')
        return redirect('listar_usuarios')

    if request.method == 'POST':
        nome = usuario.username
        usuario.delete()
        messages.success(request, f'Usuário {nome} deletado com sucesso!')
        return redirect('listar_usuarios')

    return render(request, 'usuarios/confirmar_delete_usuario.html', {'usuario': usuario})
