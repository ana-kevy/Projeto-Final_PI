from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vagas, name='lista_vagas'),
    path('nova/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
]
