from django.db import models

# Create your models here.
from apps.catalogos.empleados.models import Empleados
from apps.catalogos.tipoMovimientoCaja.models import TipoMovimientoCaja
from apps.movimiento.factura.models import Facturas
from apps.movimiento.compra.models import Compras

class Caja (models.Model):
    SaldoInicial= models.DecimalField(verbose_name='Saldo inicial',  max_digits=10,decimal_places=2)
    #Ingresos = models.DecimalField(verbose_name='Ingreso',  max_digits=10,decimal_places=2)
    Egresos = models.DecimalField(verbose_name='Egresos',  max_digits=10,decimal_places=2)
    SaldoFinal = models.DecimalField (verbose_name='Saldo final',  max_digits=10,decimal_places=2)
    FechaApertura = models.DateTimeField(verbose_name='Fecha de apertura de la caja')
    FechaCierre = models.DateTimeField(verbose_name='Fecha de cierre de la caja')
    NumCaja= models.IntegerField(verbose_name='Numero de caja')
    EmpleadoId = models.ForeignKey(Empleados,verbose_name='Empleados', on_delete=models.PROTECT)
    Din_efectivo = models.DecimalField (verbose_name='Dinero en efectivo',max_digits=10, decimal_places=2)
    Din_digital = models.DecimalField (verbose_name='Dinero en digital',max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Cajas"

    def __str__ (self):
        return f"{self.NumCaja}"

class MovimientoCaja (models.Model):
    cajaId = models.ForeignKey(Caja, verbose_name='Caja', on_delete=models.PROTECT)
    fecha = models.DateTimeField(verbose_name='Fecha')
    tipoMovimientoCajaId = models.ForeignKey(TipoMovimientoCaja, verbose_name='Tipo de movimiento', on_delete=models.PROTECT)
    monto = models.DecimalField (verbose_name='Monto',max_digits=10, decimal_places=2)
    facturaid= models.ForeignKey(Facturas,verbose_name='Factura', null=True, blank=True, on_delete=models.PROTECT)
    compraid= models.ForeignKey(Compras,verbose_name='Compra', null=True, blank=True, on_delete=models.PROTECT)
    descripcion = models.CharField (verbose_name='Descripcion', null=True, blank=True,  max_length=300)

    class Meta:
        verbose_name_plural = "Movimientos"

    def __str__ (self):
        return f"{self.cajaId}"
