from django.contrib import admin
from apps.catalogos.abono.models import Abonos

@admin.register(Abonos)
class AbonoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['FechaAbono', 'Monto', 'Detalle', 'FacturaId', 'CajaId', 'MetodoPagoId']

