"""gestao_rh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('gestao_rh.core.urls'), name='core'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('funcionarios/', include('gestao_rh.funcionarios.urls'), name='funcionarios'),
    path('documentos/', include('gestao_rh.documentos.urls'), name='documentos'),
    path('horas-extra/', include('gestao_rh.registro_hora_extra.urls'), name='horas_extra'),
    path('empresas/', include('gestao_rh.empresas.urls'), name='empresas'),
    path('departamentos/', include('gestao_rh.departamentos.urls'), name='departamentos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
