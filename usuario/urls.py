from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    # Usuários
    path('', views.UsuarioListView.as_view(), name='usuario_list'),
    path('novo/', views.UsuarioCreateView.as_view(), name='usuario_create'),
    path('<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario_detail'),
    path('<int:pk>/editar/', views.UsuarioUpdateView.as_view(), name='usuario_update'),
    path('<int:pk>/excluir/', views.UsuarioDeleteView.as_view(), name='usuario_delete'),

    # Mensagens
    path('mensagens/', views.MensagemListView.as_view(), name='mensagem_list'),
    path('mensagens/nova/', views.MensagemCreateView.as_view(), name='mensagem_create'),
]
