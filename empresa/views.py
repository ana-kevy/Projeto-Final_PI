from django.shortcuts import *
from django.contrib.auth.decorators import *
from .models import Vaga
from .forms import VagaForm

# Listar todas as vagas
def listar_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, "vaga/listar.html", {"vagas": vagas})

# Detalhar uma vaga
def detalhar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    return render(request, "vaga/detalhar.html", {"vaga": vaga})

# Criar vaga (somente empresa logada)
@login_required
def criar_vaga(request):
    if request.method == "POST":
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_vagas")
    else:
        form = VagaForm()
    return render(request, "vaga/form.html", {"form": form})

# Editar vaga
@login_required
def editar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == "POST":
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            return redirect("listar_vagas")
    else:
        form = VagaForm(instance=vaga)
    return render(request, "vaga/form.html", {"form": form})

# Excluir vaga
@login_required
def excluir_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == "POST":
        vaga.delete()
        return redirect("listar_vagas")
    return render(request, "vaga/confirmar_exclusao.html", {"vaga": vaga})