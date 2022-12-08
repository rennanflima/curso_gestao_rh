from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Empresa


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        self.object = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = self.object
        funcionario.save()
        return redirect(self.object.get_absolute_url())


class EmpresaEditView(UpdateView):
    model = Empresa
    fields = ['nome']
