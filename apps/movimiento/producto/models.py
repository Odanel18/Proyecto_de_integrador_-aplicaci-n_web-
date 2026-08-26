from django.db import models
from apps.movimiento.marca.models import Marcas
from apps.movimiento.moto.models import Motos
from apps.catalogos.categoria.models import Categorias
from apps.catalogos.size.models import Size
from apps.catalogos.ColorProducto.models import ColorProducto


class Productos(models.Model):
    
    Nombre = models.CharField(verbose_name='Nombre', max_length=50)
    CategoriaId = models.ForeignKey(Categorias, verbose_name='Categoria', on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.Nombre}"


class DetalleProductos(models.Model):

    Codigo = models.CharField(verbose_name='Código', max_length=30, null=True, blank=True)
    producto = models.ForeignKey(Productos, verbose_name='Producto', on_delete=models.PROTECT)
    MarcaId = models.ForeignKey(Marcas, verbose_name='Marca', on_delete=models.PROTECT)
    MotoId = models.ForeignKey(Motos, verbose_name='Moto', on_delete=models.PROTECT)
    size = models.ForeignKey(Size, verbose_name='Tamaño', null=True, blank=True, on_delete=models.PROTECT)
    ColorId= models.ForeignKey(ColorProducto, verbose_name='Color', null=True, blank=True, on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Detalles del producto'

    def __str__(self):
        return f"Codigo del produto {self.Codigo} - nombre {self.producto.Nombre} - marca del producto {self.MarcaId.Nombre} - modelo de moto {self.MotoId} - color {self.ColorId.Color}"

class RegistroProducto(models.Model):

    Cantidad = models.IntegerField(verbose_name='Cantidad')
    precioCosto = models.DecimalField(verbose_name='Precio de costo', max_digits=10, decimal_places=2)
    PrecioVenta = models.DecimalField(verbose_name='Precio de venta', max_digits=10, decimal_places=2)
    FechaRegistro = models.DateTimeField(verbose_name='Fecha de registro',auto_now_add=True)
    DetalleCompraId = models.ForeignKey('compra.DetalleCompra', verbose_name='Detalle de compra', on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    

    class Meta:
        verbose_name_plural = 'Registro de productos'

    def __str__(self):
        return f"Registro del producto  en la compra {self.DetalleCompraId} - Cantidad: {self.Cantidad}"
