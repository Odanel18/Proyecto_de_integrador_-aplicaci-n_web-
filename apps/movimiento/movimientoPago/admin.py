from django.contrib import admin
from apps.movimiento.movimientoPago.models import MovimientoPago

@admin.register(MovimientoPago)
class MovimientoPagoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'monto']
    list_display = ['monto', 'fecha', 'metodoPagoId', 'facturaId', 'facturaCreditoId', 'tipoMovimientoCajaId', 'origenSaldoId', 'compraId', 'compraCreditoId']