from django.contrib import admin
from apps.movimiento.factura.models import Facturas
from apps.movimiento.factura.models import DetalleFactura
@admin.register(Facturas)
class facturaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumFactura']
    list_display = ['NumFactura','Fecha', 'ClienteId','MetodoPagoId','Cajaid','Total']
# Register your models here.

@admin.register(DetalleFactura)
class detalleFacturaAdmin(admin.ModelAdmin):
    search_fields = ['id','FacturaId']
    list_display = ['Cantidad', 'Subtotal','detalleProductoId','FacturaId']
# Register your models here.i
