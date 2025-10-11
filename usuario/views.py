from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario, Mensagem


# ----- Usuário -----
class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    context_object_name = 'usuarios'


class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario


class UsuarioCreateView(CreateView):
    model = Usuario
    fields = ['username', 'first_name', 'last_name', 'email', 'cpf', 'endereco', 'curriculo', 'habilidades', 'link_portfolio', 'is_admin']
    success_url = reverse_lazy('usuario:usuario_list')


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
