from django.db import models

from apps.catalogos.clientes.models import Clientes
from apps.catalogos.metodoPago.models import MetodoPago
from apps.catalogos.condicionPago.models import CondicionPago
from apps.catalogos.estadoCuenta.models import EstadoCuenta
from apps.movimiento.producto.models import DetalleProductos

class Facturas(models.Model):
    NumFactura= models.IntegerField(verbose_name='Número de factura')
    Fecha = models.DateTimeField(verbose_name='Fecha')
    ClienteId = models.ForeignKey(Clientes, verbose_name='Clientes', on_delete=models.PROTECT)
    MetodoPagoId = models.ForeignKey(MetodoPago, verbose_name='Metodo de pago', on_delete=models.PROTECT)
    Total = models.DecimalField(verbose_name='Total',max_digits=10, decimal_places=2)
    condicionId = models.ForeignKey(CondicionPago, verbose_name='Condición del pago', on_delete=models.PROTECT)
    estadoCuentaId= models.ForeignKey(EstadoCuenta, verbose_name='Estado de la factura', on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    
    class Meta :
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f"Facturara {self.NumFactura} -  al cliente {self.ClienteId}"
    

# Create your models here.
class DetalleFactura (models.Model):
    Cantidad = models.IntegerField(verbose_name="Cantidad")
    Subtotal= models.DecimalField (verbose_name='Precio costo',max_digits=7, decimal_places=2)
    detalleProductoId = models.ForeignKey (DetalleProductos,verbose_name='Detalle de productos',on_delete=models.PROTECT)
    FacturaId= models.ForeignKey (Facturas,verbose_name="Factura",on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural="Detalles de factura"
    def __str__ (self):
        return f"{self.FacturaId}"

class FacturasCredito (models.Model):
    ClienteId = models.ForeignKey(Clientes, verbose_name='Clientes', on_delete=models.PROTECT)
    FacturaId= models.ForeignKey (Facturas,verbose_name="Factura",on_delete=models.PROTECT)
    FechaInicioCredito = models.DateTimeField(verbose_name='Fecha de inicio')
    montoTotalCredito = models.DecimalField(verbose_name='Monto total del credito', max_digits=10, decimal_places=2)
    saldoPendiente = models.DecimalField(verbose_name='Saldo pendiente',max_digits=10, decimal_places=2)
    FechaLimiteCredito = models.DateTimeField(verbose_name='Fecha limite')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'FacturasCredito'
    
    def __str__(self):
        return f'Factura al credito codigo {self.FacturaId.NumFactura}'