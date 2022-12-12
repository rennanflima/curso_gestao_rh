from django.db import models
from django.urls import reverse


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey('funcionarios.Funcionario', on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse("horas_extra:listar-banco-horas")
