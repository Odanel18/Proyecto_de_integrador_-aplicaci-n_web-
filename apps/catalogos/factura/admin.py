from django.contrib import admin
from apps.catalogos.factura.models import Facturas

@admin.register(Facturas)
class facturaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumFactura']
    list_display = ['NumFactura','Fecha', 'ClienteId','MetodoPagoId','Cajaid','Total']
# Register your models here.
