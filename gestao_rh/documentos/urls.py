from django.urls import path

from .views import EditarDocumentoView, NovoDocumentoView

app_name = 'documentos'
urlpatterns = [
    path('novo/funcionario/<int:funcionario_id>/', NovoDocumentoView.as_view(), name='novo-documento'),
    path('<int:pk>/editar/', EditarDocumentoView.as_view(), name='editar-documento'),
]
