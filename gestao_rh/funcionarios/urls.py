from django.urls import path

from .views import DeletarFuncionarioView, EditarFuncionarioView, ListaFuncionariosView, NovoFuncionarioView

app_name = 'funcionarios'
urlpatterns = [
    path('', ListaFuncionariosView.as_view(), name='lista-funcionarios'),
    path('novo/', NovoFuncionarioView.as_view(), name='novo-funcionario'),
    path('<int:pk>/editar/', EditarFuncionarioView.as_view(), name='editar-funcionario'),
    path('<int:pk>/deletar/', DeletarFuncionarioView.as_view(), name='deletar-funcionario'),
]
