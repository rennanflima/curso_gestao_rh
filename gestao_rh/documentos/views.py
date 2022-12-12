from django.views.generic import CreateView, UpdateView

from .models import Documento


class NovoDocumentoView(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']

        return self.form_valid(form) if form.is_valid() else self.form_invalid(form)


class EditarDocumentoView(UpdateView):
    model = Documento
    fields = ['descricao']
