from django.contrib import admin
from apps.catalogos.detalleCompra.models import DetalleCompra

@admin.register(DetalleCompra)
class detalleCompraAdmin(admin.ModelAdmin):
    search_fields = ['id',"CompraId"]
    list_display = ['Cantidad', 'ProductoId', 'CompraId','PrecioUnitario',"Subtotal"]
# Register your models here.
