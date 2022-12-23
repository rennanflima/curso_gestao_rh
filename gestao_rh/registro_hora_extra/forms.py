from django import forms

from .models import RegistroHoraExtra


class RegistroHoraExtraForm(forms.ModelForm):
    class Meta:
        model = RegistroHoraExtra
        fields = ['funcionario', 'horas', 'motivo',]

    def __init__(self, empresa, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = empresa.funcionario_set.all()
        if self.instance and self.instance.pk:
            self.fields['funcionario'].widget = forms.HiddenInput()

    def clean_funcionario(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return RegistroHoraExtra.objects.get(pk=instance.pk).funcionario
        else:
            return self.cleaned_data['atividade']
