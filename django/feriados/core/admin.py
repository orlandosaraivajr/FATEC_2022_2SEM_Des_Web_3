from django.contrib import admin
from .models import FeriadoModel
from datetime import date

class FeriadoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia', 'mes','modificado_em','registrado_esse_ano','feriado_esse_mes')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome', 'dia', 'mes',)
    
    def registrado_esse_ano(self, obj):
        hoje = date.today()
        return obj.modificado_em.year == hoje.year
    
    def feriado_esse_mes(self, obj):
        hoje = date.today()
        return obj.mes == hoje.month
    
    registrado_esse_ano.short_description = "Esse ano ?"
    registrado_esse_ano.boolean = True
    feriado_esse_mes.short_description = "Feriado em breve"
    feriado_esse_mes.boolean = True
    
admin.site.register(FeriadoModel, FeriadoModelAdmin)
# admin.site.register(FeriadoModel)
