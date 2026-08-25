from django.contrib import admin
from apps.movimiento.factura.models import Facturas
from apps.movimiento.factura.models import DetalleFactura
from apps.movimiento.factura.models import FacturasCredito

@admin.register(Facturas)
class facturaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumFactura']
    list_display = ['NumFactura','Fecha','condicionId','Total']
# Register your models here.

@admin.register(DetalleFactura)
class detalleFacturaAdmin(admin.ModelAdmin):
    search_fields = ['id','FacturaId']
    list_display = ['Cantidad','PrecioUnitario', 'Subtotal','loteId','FacturaId']
# Register your models here.

@admin.register(FacturasCredito)
class FacturasCreditoAdmin(admin.ModelAdmin):
    search_fields=['id', 'FacturaId']
    list_display = ['FechaInicioCredito', 'montoTotalCredito', 'saldoPendiente', 'FechaLimiteCredito']