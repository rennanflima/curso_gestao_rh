from django import forms

from .models import RegistroHoraExtra


class RegistroHoraExtraForm(forms.ModelForm):
    class Meta:
        model = RegistroHoraExtra
        fields = ['funcionario', 'horas', 'motivo',]

    def __init__(self, empresa, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = empresa.funcionario_set.all()
