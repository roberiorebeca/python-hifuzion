from django.contrib import admin
from hifuzion.contabilidade.models import PlanoConta, Cliente

admin.site.register(PlanoConta)


# admin.site.register(Cliente)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome',
                    'fone',
                    'email',
                    'conta']
    search_fields = ('nome', 'email', 'conta__nome')
