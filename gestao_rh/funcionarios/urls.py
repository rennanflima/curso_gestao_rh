from django.urls import path

from . import views

app_name = 'funcionarios'
urlpatterns = [
    path('', views.ListaFuncionariosView.as_view(), name='lista-funcionarios'),
    path('<int:pk>/editar/', views.EditarFuncionarioView.as_view(), name='editar-funcionario'),
]
