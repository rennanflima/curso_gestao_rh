from django.contrib import admin

from gestao_rh.core.decorators import admin_changelist_link

from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'departamentos_list', 'empresa', 'documentos_link')
    search_fields = ('nome', 'empresa__nome', 'user__username', )
    list_filter = ('empresa', 'departamentos')

    @admin_changelist_link('documentos', 'Documentos',
                           query_string=lambda u: f'funcionario_id={u.pk}')
    def documentos_link(self, documentos):
        return 'Documentos'
