from django.contrib import admin
from apps.movimiento.producto.models import Productos
from apps.movimiento.producto.models import DetalleProductos
from apps.movimiento.producto.models import Registro_Producto

@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Codigo']
    list_display = ['Codigo', 'Nombre','CategoriaId']
# Register your models here.

@admin.register(DetalleProductos)
class DetalleProductosAdmin(admin.ModelAdmin):
    search_fields = ['id', 'producto']
    list_display = ['producto', 'MarcaId','MotoId',"size", 'ColorId']

@admin.register(Registro_Producto)
class RegistroProductoAdmin(admin.ModelAdmin):
    search_fields=['id','DetalleCompraId']
    list_display=['DetalleCompraId','Cantidad','FechaRegistro','PrecioVenta','precioCompra']
