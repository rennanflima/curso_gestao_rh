from django.db import models
from django.urls import reverse


class Departamento(models.Model):
    nome = models.CharField(max_length=70)
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.PROTECT, default=1, related_name='departamentos')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("departamentos:lista-departamentos")
