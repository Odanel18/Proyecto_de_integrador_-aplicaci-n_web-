from django.db import models
from apps.catalogos.proveedor.models import Proveedores
from apps.catalogos.metodoPago.models import MetodoPago
from apps.movimiento.producto.models import Productos
from apps.movimiento.producto.models import DetalleProductos


# Create your models here.

class Compras (models.Model):
    Fecha= models.DateTimeField()
    MetodoPagoId= models.ForeignKey(MetodoPago,verbose_name='Metodo de pago',on_delete=models.PROTECT)
    ProveedoresId= models.ForeignKey(Proveedores,verbose_name='Proveedor',on_delete=models.PROTECT)
    NumCompra= models.IntegerField(verbose_name='Número de compra')
    Total = models.IntegerField(verbose_name="Total de la compra")
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural='Compras'

    def __str__ (self):
        return f"{self.NumCompra} - {self.ProveedoresId}" 

   
class DetalleCompra (models.Model):
    Cantidad = models.IntegerField(verbose_name="Cantidad")
    detallProductoId = models.ForeignKey (DetalleProductos,verbose_name='Detalle de Productos',on_delete=models.PROTECT)
    CompraId= models.ForeignKey (Compras,verbose_name="Compra",on_delete=models.PROTECT)
    PrecioUnitario = models.DecimalField (verbose_name='Precio costo',max_digits=7, decimal_places=2)
    Subtotal= models.DecimalField (verbose_name='Subtotal', max_digits=7, decimal_places=2)
    estado = models.BooleanField(default=True)

class Meta:
    verbose_name_plural='Detalles de compra'

def __str__ (self):
    return f"{self.CompraId}"