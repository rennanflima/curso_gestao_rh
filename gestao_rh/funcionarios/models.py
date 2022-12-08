from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField('departamentos.Departamento')
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
