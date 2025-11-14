from django.contrib import admin

from apps.catalogos.compra.models import Compras

@admin.register(Compras)
class compraAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumCompra']
    list_display = ['Fecha', 'MetodoPagoId', 'ProveedoresId','NumCompra','Total']
# Register your models here.

