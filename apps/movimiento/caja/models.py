from django.db import models
from apps.catalogos.empleados.models import Empleados
from apps.catalogos.tipoMovimientoCaja.models import TipoMovimientoCaja
from apps.movimiento.factura.models import Facturas,FacturasCredito
from apps.movimiento.compra.models import Compras,ComprasCredito

class Caja (models.Model):
    NumCaja= models.IntegerField(verbose_name='Numero de caja')
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Cajas"

    def __str__ (self):
        return f"{self.NumCaja}"
    
class TurnoCaja (models.Model):
    SaldoInicial= models.DecimalField(verbose_name='Saldo inicial',  max_digits=10,decimal_places=2)
    Egresos = models.DecimalField(verbose_name='Egresos',  max_digits=10,decimal_places=2)
    SaldoFinal = models.DecimalField (verbose_name='Saldo final',  max_digits=10,decimal_places=2)
    FechaApertura = models.DateTimeField(verbose_name='Fecha de apertura de la caja')
    FechaCierre = models.DateTimeField(verbose_name='Fecha de cierre de la caja')
    NumCajaid= models.ForeignKey(Caja, verbose_name='Numero de caja', on_delete=models.PROTECT)
    EmpleadoId = models.ForeignKey(Empleados,verbose_name='Empleados', on_delete=models.PROTECT)
    Din_efectivo = models.DecimalField (verbose_name='Dinero en efectivo',max_digits=10, decimal_places=2)
    Din_digital = models.DecimalField (verbose_name='Dinero en digital',max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Cajas"

    def __str__ (self):
        return f"{self.EmpleadoId} - {self.FechaApertura} - {self.FechaCierre}"

class MovimientoCaja (models.Model):
    
    fecha = models.DateTimeField(verbose_name='Fecha')
    descripcion = models.CharField (verbose_name='Descripcion', null=True, blank=True,  max_length=300)
    monto = models.DecimalField (verbose_name='Monto',max_digits=10, decimal_places=2)
    tipoMovimientoCajaId = models.ForeignKey(TipoMovimientoCaja, verbose_name='Tipo de movimiento', on_delete=models.PROTECT)
    facturaid= models.ForeignKey(Facturas,verbose_name='Factura', null=True, blank=True, on_delete=models.PROTECT)
    compraid= models.ForeignKey(Compras,verbose_name='Compra', null=True, blank=True, on_delete=models.PROTECT)
    compraCreditoId= models.ForeignKey(ComprasCredito, verbose_name='Compra al credito', null=True, blank=True, on_delete=models.PROTECT)
    facturaCreditoId = models.ForeignKey(FacturasCredito, verbose_name='Factura al credito', null=True, blank=True, on_delete=models.PROTECT)
    turnoCajaId = models.ForeignKey(TurnoCaja, verbose_name='Turno de caja', on_delete=models.PROTECT)
    estado= models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Movimientos"

    def __str__ (self):
        return f"{self.turnoCajaId} - {self.tipoMovimientoCajaId} - {self.monto}"
