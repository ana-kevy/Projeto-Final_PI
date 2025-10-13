from django.urls import path
from . import views


app_name = 'vagas'

urlpatterns = [
    path('', views.listar_vagas, name='listar_vagas'),
    path('criar/', views.criar_vaga, name='criar_vaga'),
    path('editar/<int:pk>/', views.editar_vaga, name='editar_vaga'),
    path('deletar/<int:pk>/', views.deletar_vaga, name='deletar_vaga'),
    path('<int:vaga_id>/mensagens/', views.enviar_mensagem, name='enviar_mensagem'),
]
