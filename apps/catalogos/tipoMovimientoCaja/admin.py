from django.contrib import admin
from apps.catalogos.tipoMovimientoCaja.models import TipoMovimientoCaja

@admin.register(TipoMovimientoCaja)
class TipoMovimientoCajaAdmin (admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Tipo']
    
