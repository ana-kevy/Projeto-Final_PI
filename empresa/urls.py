from django.urls import path
from . import views

app_name = 'empresa'

urlpatterns = [
    path('', views.EmpresaListView.as_view(), name='empresa_list'),
    path('nova/', views.EmpresaCreateView.as_view(), name='empresa_create'),
    path('<int:pk>/', views.EmpresaDetailView.as_view(), name='empresa_detail'),
    path('<int:pk>/editar/', views.EmpresaUpdateView.as_view(), name='empresa_update'),
    path('<int:pk>/excluir/', views.EmpresaDeleteView.as_view(), name='empresa_delete'),
]
