from django.urls import path

from .views import (MarcarHoraExtraNaoUtilizada, MarcarHoraExtraUtilizada, RegistroHoraExtraCreateView, RegistroHoraExtraDeleteView,
                    RegistroHoraExtraFuncionarioNovoView, RegistroHoraExtraListView, RegistroHoraExtraUpdateView)

app_name = 'horas_extra'
urlpatterns = [
    path('', RegistroHoraExtraListView.as_view(), name='listar-banco-horas'),
    path('novo/', RegistroHoraExtraCreateView.as_view(), name='registro-hora-extra'),
    path('novo/funcionario/<int:funcionario_id>/', RegistroHoraExtraFuncionarioNovoView.as_view(), name='novo-registro-hora-extra'),
    path('<int:pk>/editar/', RegistroHoraExtraUpdateView.as_view(), name='editar-registro-hora-extra'),
    path('<int:pk>/funcionario/<int:funcionario_id>/editar/', RegistroHoraExtraUpdateView.as_view(), name='editar-registro-hora-extra-funcionario'),
    path('<int:pk>/deletar/', RegistroHoraExtraDeleteView.as_view(), name='deletar-registro-hora-extra'),
    path('<int:pk>/funcionario/<int:funcionario_id>/deletar/', RegistroHoraExtraDeleteView.as_view(), name='deletar-registro-hora-extra-funcionario'),

    path('<int:pk>/marcar-utilizada/', MarcarHoraExtraUtilizada.as_view(), name='marcar-hora-extra-utilizada'),
    path('<int:pk>/marcar-nao-utilizada/', MarcarHoraExtraNaoUtilizada.as_view(), name='marcar-hora-extra-nao-utilizada'),
]
