from django.urls import path
from . import views

urlpatterns = [
    path("vagas/", views.listar_vagas, name="listar_vagas"),
    path("vagas/<int:pk>/", views.detalhar_vaga, name="detalhar_vaga"),
    path("vagas/criar/", views.criar_vaga, name="criar_vaga"),
    path("vagas/<int:pk>/editar/", views.editar_vaga, name="editar_vaga"),
    path("vagas/<int:pk>/excluir/", views.excluir_vaga, name="excluir_vaga"),
]