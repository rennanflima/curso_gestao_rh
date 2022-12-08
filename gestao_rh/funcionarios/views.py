from django.views.generic import ListView, UpdateView


class ListaFuncionariosView(ListView):
    context_object_name = 'funcionarios'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return empresa_logada.funcionario_set.all()


class EditarFuncionarioView(UpdateView):
    fields = ['usuario__first_name', 'usuario__last_name', 'departamentos']

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return empresa_logada.funcionario_set.all()
