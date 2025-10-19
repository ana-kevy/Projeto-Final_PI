from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vaga, Mensagem
from .forms import VagaForm, MensagemForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from empresa.models import Empresa

# Permitir apenas usuários do tipo empresa criarem vagas
def is_empresa(user):
    return user.is_authenticated and getattr(user, "is_empresa", False)

# LISTAR VAGAS (todos os usuários podem visualizar)
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


# CRIAR VAGA (apenas empresa logada)

@login_required
@user_passes_test(is_empresa)
def criar_vaga(request):
    empresa = Empresa.objects.filter(nome=request.user.username).first()

    if not empresa:
        messages.error(request, 'Você precisa ter um perfil de empresa cadastrado para criar vagas.')
        return redirect('listar_vagas')

    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            vaga = form.save(commit=False)
            vaga.empresa = empresa  # ✅ vincula à empresa logada automaticamente
            vaga.save()
            messages.success(request, 'Vaga cadastrada com sucesso!')
            return redirect('listar_vagas')
        else:
            messages.error(request, 'Erro ao cadastrar vaga.')
    else:
        form = VagaForm()
    return render(request, 'vagas/form.html', {'form': form, 'titulo': 'Cadastrar Vaga'})

# EDITAR VAGA (empresa só pode editar suas próprias vagas)

@login_required
@user_passes_test(is_empresa)
def editar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)

    #  Segurança: empresa só pode editar suas vagas
    empresa = Empresa.objects.filter(nome=request.user.username).first()
    if vaga.empresa != empresa:
        messages.error(request, 'Você não tem permissão para editar esta vaga.')
        return redirect('listar_vagas')

    form = VagaForm(request.POST or None, instance=vaga)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Vaga atualizada com sucesso!')
        return redirect('listar_vagas')

    return render(request, 'vagas/form.html', {'form': form, 'titulo': 'Editar Vaga'})


# DELETAR VAGA (empresa só pode deletar suas vagas)
@login_required
@user_passes_test(is_empresa)
def deletar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)

    empresa = Empresa.objects.filter(nome=request.user.username).first()
    if vaga.empresa != empresa:
        messages.error(request, 'Você não tem permissão para excluir esta vaga.')
        return redirect('listar_vagas')

    if request.method == 'POST':
        vaga.delete()
        messages.success(request, 'Vaga excluída com sucesso!')
        return redirect('listar_vagas')

    return render(request, 'vagas/confirmar_delete.html', {'vaga': vaga})

# ENVIAR MENSAGEM (candidatos enviam para empresa)
@login_required
def enviar_mensagem(request, vaga_id):
    vaga = get_object_or_404(Vaga, pk=vaga_id)

    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.vaga = vaga
            mensagem.empresa = vaga.empresa  # ✅ empresa definida automaticamente
            mensagem.candidato = request.user  # ✅ candidato logado
            mensagem.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('detalhar_vaga', pk=vaga.id)
        else:
            messages.error(request, 'Erro ao enviar mensagem.')
    else:
        form = MensagemForm()

    mensagens_vaga = Mensagem.objects.filter(vaga=vaga).order_by('data_envio')
    return render(request, 'vagas/mensagens.html', {'vaga': vaga, 'form': form, 'mensagens': mensagens_vaga})
