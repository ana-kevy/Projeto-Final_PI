from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empresas, name='listar_empresas'),
    path('<int:id>/', views.detalhes_empresa, name='detalhes_empresa'),
]
