from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vaga, Candidatura


# ----- VAGAS -----
class VagaListView(ListView):
    model = Vaga
    context_object_name = 'vagas'

class VagaDetailView(DetailView):
    model = Vaga

class VagaCreateView(LoginRequiredMixin, CreateView):
    model = Vaga
    fields = ['titulo', 'requisitos', 'local', 'tipo', 'remuneracao', 'carga_horaria', 'empresa']
    success_url = reverse_lazy('vagas:vaga_list')

class VagaUpdateView(LoginRequiredMixin, UpdateView):
    model = Vaga
    fields = ['titulo', 'requisitos', 'local', 'tipo', 'remuneracao', 'carga_horaria', 'empresa']
    success_url = reverse_lazy('vagas:vaga_list')

class VagaDeleteView(LoginRequiredMixin, DeleteView):
    model = Vaga
    success_url = reverse_lazy('vagas:vaga_list')


# ----- CANDIDATURAS -----
class CandidaturaCreateView(LoginRequiredMixin, CreateView):
    model = Candidatura
    fields = ['vaga']
    success_url = reverse_lazy('vagas:minhas_candidaturas')

    def form_valid(self, form):
        form.instance.candidato = self.request.user
        return super().form_valid(form)


class CandidaturaListView(LoginRequiredMixin, ListView):
    model = Candidatura
    context_object_name = 'candidaturas'

    def get_queryset(self):
        return Candidatura.objects.filter(candidato=self.request.user)


class CandidaturaDetailView(LoginRequiredMixin, DetailView):
    model = Candidatura
