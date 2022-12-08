from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField('departamentos.Departamento')
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.usuario.get_full_name()
