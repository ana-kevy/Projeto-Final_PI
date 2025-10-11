from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Empresa

class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    context_object_name = 'empresas'

class EmpresaDetailView(LoginRequiredMixin, DetailView):
    model = Empresa

class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = ['razao_social', 'cnpj', 'endereco', 'area_atuacao', 'email', 'senha']
    success_url = reverse_lazy('empresa:empresa_list')

class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = ['razao_social', 'cnpj', 'endereco', 'area_atuacao', 'email', 'senha']
    success_url = reverse_lazy('empresa:empresa_list')

class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresa:empresa_list')
