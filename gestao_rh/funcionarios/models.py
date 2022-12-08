from django.db import models

# User = get_user_model()
User = None


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField('departamentos.Departamento')
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.usuario.get_full_name()

    def departamentos_list(self):
        return ', '.join([d.nome for d in self.departamentos.all()])
    departamentos_list.short_description = "Departamentos"
