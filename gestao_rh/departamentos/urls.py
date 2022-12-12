from django.urls import path

from .views import DeletarDepartamentoView, EditarDepartamentoView, ListaDepartamentosView, NovoDepartamentoView

app_name = 'departamentos'
urlpatterns = [
    path('', ListaDepartamentosView.as_view(), name='lista-departamentos'),
    path('novo/', NovoDepartamentoView.as_view(), name='novo-departamento'),
    path('<int:pk>/editar/', EditarDepartamentoView.as_view(), name='editar-departamento'),
    path('<int:pk>/deletar/', DeletarDepartamentoView.as_view(), name='deletar-departamento'),
]
