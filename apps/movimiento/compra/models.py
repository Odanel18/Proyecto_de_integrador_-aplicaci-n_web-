from django.db import models
from apps.catalogos.proveedor.models import Proveedores
from apps.catalogos.condicionPago.models import CondicionPago
from apps.catalogos.estadoCuenta.models import EstadoCuenta

class Compras (models.Model):
    NumCompra= models.CharField(verbose_name='Número de compra', max_length=100)
    Fecha= models.DateField()
    Total = models.DecimalField(verbose_name="Total de la compra", max_digits=10, decimal_places=2)
    CondicionPagoId = models.ForeignKey(CondicionPago, verbose_name='Condición del pago', on_delete=models.PROTECT)
    ProveedorId= models.ForeignKey(Proveedores,verbose_name='Proveedor',on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural='Compras'

    def __str__ (self):
        return f"Compra número {self.NumCompra} - al proveedor {self.ProveedorId}" 

   
class DetalleCompra (models.Model):
    Cantidad = models.IntegerField(verbose_name="Cantidad")
    DetalleProductoId = models.ForeignKey('producto.DetalleProductos', verbose_name='Detalle de Productos', on_delete=models.PROTECT)
    CompraId= models.ForeignKey (Compras,related_name='detallesCompra',verbose_name="Compra",on_delete=models.PROTECT)
    PrecioUnitario = models.DecimalField (verbose_name='Precio costo',max_digits=7, decimal_places=2)
    Subtotal= models.DecimalField (verbose_name='Subtotal', max_digits=7, decimal_places=2)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural='Detalles de compra'

    def __str__ (self):
        return f"{self.CompraId}"

class ComprasCredito (models.Model):
    CompraId= models.ForeignKey (Compras,verbose_name="Compra",on_delete=models.PROTECT)
    FechaInicio = models.DateField(verbose_name='Fecha de inicio')
    MontoTotal = models.DecimalField(verbose_name='Monto total del credito', max_digits=10, decimal_places=2)
    SaldoPendiente = models.DecimalField(verbose_name='Saldo pendiente',max_digits=10, decimal_places=2)
    FechaVencimiento = models.DateField(verbose_name='Fecha limite')
    EstadoCuentaId= models.ForeignKey(EstadoCuenta, verbose_name='Estado de la factura', on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'ComprasCredito'
    
    def __str__(self):
        return f'Factura al credito codigo {self.CompraId.NumCompra}'