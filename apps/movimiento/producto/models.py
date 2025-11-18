from django.db import models
from apps.movimiento.marca.models import Marcas
from apps.movimiento.moto.models import Motos
from apps.catalogos.categoria.models import Categorias
from apps.catalogos.size.models import Size


class Productos(models.Model):
    Codigo = models.CharField(verbose_name='Código', max_length=30)
    Nombre = models.CharField(verbose_name='Nombre', max_length=50)
    CategoriaId = models.ForeignKey(Categorias, verbose_name='Categoria', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.Codigo} - {self.Nombre}"


class DetalleProductos(models.Model):
    producto = models.ForeignKey(Productos, verbose_name='Producto', on_delete=models.PROTECT)
    MarcaId = models.ForeignKey(Marcas, verbose_name='Marca', on_delete=models.PROTECT)
    MotoId = models.ForeignKey(Motos, verbose_name='Moto', on_delete=models.PROTECT)
    PrecioVenta = models.DecimalField(verbose_name='Precio de venta', max_digits=10, decimal_places=2)
    precioCompra = models.DecimalField(verbose_name='Precio de compra', max_digits=10, decimal_places=2)
    Stock = models.IntegerField(verbose_name='Stock')
    size = models.ForeignKey(Size, verbose_name='Tamaño', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Detalles del producto'

    def __str__(self):
        return f"Detalle del producto {self.producto}"
