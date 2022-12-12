import os

from django.db import models
from django.urls import reverse
from django.utils import timezone


def arquivo_documento_directory_path(instance, filename):
    """File will be uploaded to MEDIA_ROOT/arquivos/edital_<id>/<filename>"""
    filename_base, filename_ext = os.path.splitext(filename)
    now = timezone.now()
    return f'documentos/funcionario_{instance.funcionario.pk}/{now:%Y%m%d%H%M%S}{filename_ext.lower()}'


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    funcionario = models.ForeignKey('funcionarios.Funcionario', on_delete=models.PROTECT, related_name='documentos')
    arquivo = models.FileField(upload_to=arquivo_documento_directory_path, default='')

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse("funcionarios:editar-funcionario", kwargs={'pk': self.funcionario.pk})
