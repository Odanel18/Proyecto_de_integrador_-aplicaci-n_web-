from django.contrib import admin
from apps.catalogos.producto.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'codigo']
    list_display = ['codigo', 'nombre','precio_venta','marcaId','stock','motoid','categoriaId']
# Register your models here.
