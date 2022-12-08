from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from gestao_rh.funcionarios.models import Funcionario


@login_required
def home(request):
    return render(request, 'core/index.html')
