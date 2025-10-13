from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empresas, name='listar_empresas'),
    path('criar/', views.criar_empresa, name='criar_empresa'),
    path('editar/<int:pk>/', views.editar_empresa, name='editar_empresa'),
    path('deletar/<int:pk>/', views.deletar_empresa, name='deletar_empresa'),
]
