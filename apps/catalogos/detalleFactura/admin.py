from django.contrib import admin
from apps.catalogos.detalleFactura.models import DetalleFactura

@admin.register(DetalleFactura)
class detalleFacturaAdmin(admin.ModelAdmin):
    search_fields = ['id','FacturaId']
    list_display = ['Cantidad', 'Subtotal','ProductoId','FacturaId']
# Register your models here.i

 