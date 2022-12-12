from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import FuncionarioForm
from .models import Funcionario

User = get_user_model()


class ListaFuncionariosView(ListView):
    context_object_name = 'funcionarios'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return empresa_logada.funcionario_set.all()


class NovoFuncionarioView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        funcionario = form.save(commit=False)
        username = nome.strip().split(' ')[0] + nome.strip().split(' ')[-1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.usuario = User.objects.create_user(username=username, name=nome)
        funcionario.save()
        return super().form_valid(form)


class EditarFuncionarioView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return empresa_logada.funcionario_set.all()


class DeletarFuncionarioView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:lista-funcionarios')

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return empresa_logada.funcionario_set.all()
