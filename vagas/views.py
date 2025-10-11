from django.http import HttpResponse

def lista_vagas(request):
    return HttpResponse("Listagem de vagas")

def cadastrar_vaga(request):
    return HttpResponse("Página para cadastrar vaga")

def enviar_mensagem(request):
    return HttpResponse("Página para enviar mensagem")
