from django.db import models
from apps.catalogos.proveedor.models import Proveedores
from apps.catalogos.condicionPago.models import CondicionPago
from apps.catalogos.estadoCuenta.models import EstadoCuenta
from apps.movimiento.producto.models import DetalleProductos


# Create your models here.

class Compras (models.Model):
    NumCompra= models.IntegerField(verbose_name='Número de compra')
    Fecha= models.DateTimeField()
    Total = models.IntegerField(verbose_name="Total de la compra")
    condicionId = models.ForeignKey(CondicionPago, verbose_name='Condición del pago', on_delete=models.PROTECT)
    estadoCuentaId= models.ForeignKey(EstadoCuenta, verbose_name='Estado de la factura', on_delete=models.PROTECT)
    ProveedoresId= models.ForeignKey(Proveedores,verbose_name='Proveedor',on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural='Compras'

    def __str__ (self):
        return f"Compra número {self.NumCompra} - al proveedor {self.ProveedoresId}" 

   
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

class ComprasCredito (models.Model):
    ProveedoresId = models.ForeignKey(Proveedores, verbose_name='Proveedores', on_delete=models.PROTECT)
    CompraId= models.ForeignKey (Compras,verbose_name="Compra",on_delete=models.PROTECT)
    FechaInicioCredito = models.DateTimeField(verbose_name='Fecha de inicio')
    montoTotalCredito = models.DecimalField(verbose_name='Monto total del credito', max_digits=10, decimal_places=2)
    saldoPendiente = models.DecimalField(verbose_name='Saldo pendiente',max_digits=10, decimal_places=2)
    FechaLimiteCredito = models.DateTimeField(verbose_name='Fecha limite')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'ComprasCredito'
    
    def __str__(self):
        return f'Factura al credito codigo {self.CompraId.NumCompra}'