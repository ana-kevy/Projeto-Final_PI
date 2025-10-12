from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vaga, Mensagem
from .forms import VagaForm, MensagemForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def listar_vagas(request):
    vagas = Vaga.objects.filter(ativo=True).order_by('-data_publicacao')

    paginator = Paginator(vagas, 9)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'vagas/listar.html', {'vagas': page_obj})

@login_required
def criar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaga cadastrada com sucesso!')
            return redirect('listar_vagas')
        else:
            messages.error(request, 'Erro ao cadastrar vaga.')
    else:
        form = VagaForm()
    return render(request, 'vagas/form.html', {'form': form, 'titulo': 'Cadastrar Vaga'})

@login_required
def editar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaga atualizada com sucesso!')
            return redirect('listar_vagas')
    else:
        form = VagaForm(instance=vaga)
    return render(request, 'vagas/form.html', {'form': form, 'titulo': 'Editar Vaga'})

@login_required
def deletar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        vaga.delete()
        messages.success(request, 'Vaga excluída com sucesso!')
        return redirect('listar_vagas')
    return render(request, 'vagas/confirmar_delete.html', {'vaga': vaga})

@login_required
def enviar_mensagem(request, vaga_id):
    vaga = get_object_or_404(Vaga, pk=vaga_id)
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.vaga = vaga
            mensagem.candidato = request.user
            mensagem.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('detalhar_vaga', pk=vaga.id)
        else:
            messages.error(request, 'Erro ao enviar mensagem.')
    else:
        form = MensagemForm(initial={'vaga': vaga, 'empresa': vaga.empresa})
    mensagens_vaga = Mensagem.objects.filter(vaga=vaga).order_by('data_envio')
    return render(request, 'vagas/mensagens.html', {'vaga': vaga, 'form': form, 'mensagens': mensagens_vaga})
