from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UsuarioForm, LoginForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao registrar usuário. Verifique os campos.')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/registrar.html', {'form': form, 'titulo': 'Registrar'})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {user.username}!')
                return redirect('listar_vagas')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
    else:
        form = LoginForm()
    return render(request, 'usuario/login.html', {'form': form, 'titulo': 'Login'})

def logout_usuario(request):
    logout(request)
    messages.info(request, 'Logout realizado com sucesso.')
    return redirect('login')
