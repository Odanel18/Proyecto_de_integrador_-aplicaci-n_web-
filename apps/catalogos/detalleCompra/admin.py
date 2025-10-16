from django.contrib import admin
from apps.catalogos.detalleCompra.models import DetalleCompra

@admin.register(DetalleCompra)
class detalleCompraAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['compraid', 'productoid', 'cantidad','Precio_costo']
# Register your models here.
