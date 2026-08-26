from django.contrib import admin
from apps.movimiento.producto.models import Productos
from apps.movimiento.producto.models import DetalleProductos
from apps.movimiento.producto.models import RegistroProducto

@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Nombre']
    list_display = ['Nombre','CategoriaId']
# Register your models here.

@admin.register(DetalleProductos)
class DetalleProductosAdmin(admin.ModelAdmin):
    search_fields = ['id', 'producto']
    list_display = ['producto', 'Codigo', 'MarcaId','MotoId',"size", 'ColorId']

@admin.register(RegistroProducto)
class RegistroProductoAdmin(admin.ModelAdmin):
    search_fields=['id','DetalleCompraId']
    list_display=['DetalleCompraId','Cantidad','FechaRegistro','PrecioVenta','precioCosto']
