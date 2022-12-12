from django.urls import path

from .views import RegistroHoraExtraCreateView, RegistroHoraExtraDeleteView, RegistroHoraExtraListView, RegistroHoraExtraUpdateView

app_name = 'horas_extra'
urlpatterns = [
    path('', RegistroHoraExtraListView.as_view(), name='listar-banco-horas'),
    path('novo/', RegistroHoraExtraCreateView.as_view(), name='registro-hora-extra'),
    path('<int:pk>/editar/', RegistroHoraExtraUpdateView.as_view(), name='editar-registro-hora-extra'),
    path('<int:pk>/deletar/', RegistroHoraExtraDeleteView.as_view(), name='deletar-registro-hora-extra'),
]
