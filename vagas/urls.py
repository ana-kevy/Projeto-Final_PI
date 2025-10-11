from django.urls import path
from . import views

app_name = 'vagas'

urlpatterns = [
    path('', views.VagaListView.as_view(), name='vaga_list'),
    path('nova/', views.VagaCreateView.as_view(), name='vaga_create'),
    path('<int:pk>/', views.VagaDetailView.as_view(), name='vaga_detail'),
    path('<int:pk>/editar/', views.VagaUpdateView.as_view(), name='vaga_update'),
    path('<int:pk>/excluir/', views.VagaDeleteView.as_view(), name='vaga_delete'),

    # candidaturas
    path('candidatar/', views.CandidaturaCreateView.as_view(), name='candidatar'),
    path('minhas-candidaturas/', views.CandidaturaListView.as_view(), name='minhas_candidaturas'),
    path('candidatura/<int:pk>/', views.CandidaturaDetailView.as_view(), name='candidatura_detail'),
]
