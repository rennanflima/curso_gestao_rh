from django.urls import path

from . import views

app_name = 'empresas'
urlpatterns = [
    path('nova/', views.EmpresaCreateView.as_view(), name='nova-empresa'),
    path('<int:pk>/editar/', views.EmpresaEditView.as_view(), name='editar-empresa'),
]
