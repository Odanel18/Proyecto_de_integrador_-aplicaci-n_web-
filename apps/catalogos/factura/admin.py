from django.contrib import admin
from apps.catalogos.factura.models import factura

@admin.register(factura)
class facturaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'num_Factura']
    list_display = ['num_Factura', 'clienteId','total','Metodo_PagoId','cajaid','fecha']
# Register your models here.