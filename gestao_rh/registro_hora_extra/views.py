import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View

from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra


class RegistroHoraExtraListView(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class RegistroHoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'empresa': self.request.user.funcionario.empresa})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        return context


class RegistroHoraExtraUpdateView(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_queryset(self):
        if 'funcionario_id' in self.kwargs:
            return RegistroHoraExtra.objects.filter(funcionario_id=self.kwargs['funcionario_id'])
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'empresa': self.request.user.funcionario.empresa})
        return kwargs

    def get_success_url(self):
        if 'funcionario_id' in self.kwargs:
            return reverse('funcionarios:editar-funcionario', kwargs={'pk': self.kwargs['funcionario_id']})
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        return context


class RegistroHoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('horas_extra:listar-banco-horas')

    def get_queryset(self):
        if 'funcionario_id' in self.kwargs:
            return RegistroHoraExtra.objects.filter(funcionario_id=self.kwargs['funcionario_id'])
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

    def get_success_url(self):
        if 'funcionario_id' in self.kwargs:
            return reverse('funcionarios:editar-funcionario', kwargs={'pk': self.kwargs['funcionario_id']})
        return super().get_success_url()


class RegistroHoraExtraFuncionarioNovoView(CreateView):
    model = RegistroHoraExtra
    fields = ['horas', 'motivo',]

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']

        return self.form_valid(form) if form.is_valid() else self.form_invalid(form)

    def get_success_url(self):
        return reverse('funcionarios:editar-funcionario', kwargs={'pk': self.kwargs['funcionario_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        return context


class MarcarHoraExtraUtilizada(View):
    def post(self, request, *args, **kwargs):
        registro_hora_extra = get_object_or_404(RegistroHoraExtra, pk=self.kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save(update_fields=['utilizada'])

        response = json.dumps({
            'mensagem': 'Requisição executada com sucesso!',
        })
        return HttpResponse(response, content_type='application/json')


class MarcarHoraExtraNaoUtilizada(View):
    def post(self, request, *args, **kwargs):
        registro_hora_extra = get_object_or_404(RegistroHoraExtra, pk=self.kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save(update_fields=['utilizada'])

        response = json.dumps({
            'mensagem': 'Requisição executada com sucesso!',
        })
        return HttpResponse(response, content_type='application/json')
