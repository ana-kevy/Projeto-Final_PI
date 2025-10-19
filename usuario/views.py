from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import LoginForm
from vagas.models import Mensagem


# ----- Usuário -----
class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    context_object_name = 'usuarios'


class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario


class UsuarioCreateView(CreateView):
    model = Usuario
    fields = ['username', 'first_name', 'last_name', 'email', 'cpf', 'endereco', 'curriculo', 'habilidades', 'link_portfolio', 'is_admin']
    template_name = 'cadastro_usuario.html'
    success_url = reverse_lazy('usuario:usuario_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cadastro realizado com sucesso! Faça login para continuar.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija os erros abaixo.')
        return super().form_invalid(self, form)


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['first_name', 'last_name', 'email', 'cpf', 'endereco', 'curriculo', 'habilidades', 'link_portfolio', 'is_admin']
    success_url = reverse_lazy('usuario:usuario_list')


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario:usuario_list')


# ----- Mensagem -----
class MensagemListView(LoginRequiredMixin, ListView):
    model = Mensagem
    context_object_name = 'mensagens'

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.is_staff:
            return Mensagem.objects.all()
        return Mensagem.objects.filter(candidato=user)


class MensagemCreateView(LoginRequiredMixin, CreateView):
    model = Mensagem
    fields = ['empresa', 'conteudo']
    success_url = reverse_lazy('usuario:mensagem_list')

    def form_valid(self, form):
        form.instance.candidato = self.request.user
        return super().form_valid(form)


def login(request):
    if request.user.is_authenticated:
        return redirect('listar_vagas')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')
                
                # Redireciona para a página solicitada ou para listar_vagas
                next_page = request.GET.get('next', 'listar_vagas')
                return redirect(next_page)
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
