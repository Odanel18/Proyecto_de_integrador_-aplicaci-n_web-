from django.contrib import admin

from apps.movimiento.compra.models import Compras
from apps.movimiento.compra.models import DetalleCompra

@admin.register(Compras)
class compraAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumCompra']
    list_display = ['Fecha', 'MetodoPagoId', 'ProveedoresId','NumCompra','Total']
# Register your models here.


@admin.register(DetalleCompra)
class detalleCompraAdmin(admin.ModelAdmin):
    search_fields = ['id',"CompraId"]
    list_display = ['Cantidad', 'detallProductoId', 'CompraId','PrecioUnitario',"Subtotal"]
# Register your models here.
