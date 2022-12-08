from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey('funcionarios.Funcionario', on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo
