from django import forms

from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=150, required=False)
    field_order = ['nome', 'departamentos']

    class Meta:
        model = Funcionario
        fields = ['departamentos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.usuario:
                self.fields['nome'].initial = self.instance.usuario.name

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance and instance.pk:
            if instance.usuario:
                instance.usuario.name = self.cleaned_data['nome']
        if commit:
            instance.save()
            self.save_m2m()
        return instance
