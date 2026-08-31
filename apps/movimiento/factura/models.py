from django.db import models
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.condicionPago.models import CondicionPago
from apps.catalogos.estadoCuenta.models import EstadoCuenta
from apps.movimiento.producto.models import RegistroProducto

class Facturas(models.Model):
    NumFactura= models.IntegerField(verbose_name='Número de factura')
    Fecha = models.DateTimeField(auto_now_add=True,verbose_name='Fecha')
    Total = models.DecimalField(verbose_name='Total',max_digits=10, decimal_places=2)
    ClienteId = models.ForeignKey(Clientes, verbose_name='Clientes', on_delete=models.PROTECT)
    condicionId = models.ForeignKey(CondicionPago, verbose_name='Condición del pago', on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    
    class Meta :
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f"Factura {self.NumFactura} -  al cliente {self.ClienteId}"
    

class DetalleFactura (models.Model):
    Cantidad = models.IntegerField(verbose_name="Cantidad")
    PrecioUnitario = models.DecimalField (verbose_name='Precio unitario',max_digits=7, decimal_places=2)
    Subtotal= models.DecimalField (verbose_name='Subtotal',max_digits=7, decimal_places=2)
    loteId = models.ForeignKey (RegistroProducto,verbose_name='Detalle de productos',on_delete=models.PROTECT)
    FacturaId= models.ForeignKey (Facturas,related_name='detalles',verbose_name="Factura",on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural="Detalles de factura"
    def __str__ (self):
        return f"{self.FacturaId}"

class FacturasCredito (models.Model):
    FacturaId= models.ForeignKey (Facturas,verbose_name="Factura",on_delete=models.PROTECT)
    FechaInicioCredito = models.DateTimeField(verbose_name='Fecha de inicio')
    montoTotalCredito = models.DecimalField(verbose_name='Monto total del credito', max_digits=10, decimal_places=2)
    saldoPendiente = models.DecimalField(verbose_name='Saldo pendiente',max_digits=10, decimal_places=2)
    FechaLimiteCredito = models.DateTimeField(verbose_name='Fecha limite')
    estadoCuentaId= models.ForeignKey(EstadoCuenta, verbose_name='Estado de la factura', on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'FacturasCredito'
    
    def __str__(self):
        return f'Número de factura al crédito {self.FacturaId.NumFactura} - al cliente {self.FacturaId.ClienteId}'