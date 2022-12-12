from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Departamento


class ListaDepartamentosView(ListView):
    context_object_name = 'departamentos'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return empresa_logada.departamentos.all()


class NovoDepartamentoView(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        empresa_logada = self.request.user.funcionario.empresa
        departamento.empresa = empresa_logada
        return super().form_valid(form)


class EditarDepartamentoView(UpdateView):
    model = Departamento
    fields = ['nome']

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return empresa_logada.departamentos.all()


class DeletarDepartamentoView(DeleteView):
    model = Departamento
    success_url = reverse_lazy('departamentos:lista-departamentos')

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return empresa_logada.departamentos.all()
