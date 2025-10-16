from django.contrib import admin
from apps.catalogos.detalleFactura.models import DetalleFactura

@admin.register(DetalleFactura)
class detalleFacturaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['facturaid', 'productoid','cantidad','total']
# Register your models here.
