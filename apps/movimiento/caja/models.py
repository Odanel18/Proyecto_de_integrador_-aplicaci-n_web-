from django.db import models

# Create your models here.
from apps.catalogos.empleados.models import Empleados

class Caja (models.Model):
    SaldoInicial= models.DecimalField(verbose_name='Saldo inicial',  max_digits=10,decimal_places=2)
    Ingresos = models.DecimalField(verbose_name='Ingreso',  max_digits=10,decimal_places=2)
    Egresos = models.DecimalField(verbose_name='Egresos',  max_digits=10,decimal_places=2)
    SaldoFinal = models.DecimalField (verbose_name='Saldo final',  max_digits=10,decimal_places=2)
    Fecha = models.DateTimeField()
    NumCaja= models.IntegerField(verbose_name='Numero de caja')
    EmpleadoId = models.ForeignKey(Empleados,verbose_name='Empleados', on_delete=models.PROTECT)
    Dinero = models.DecimalField (verbose_name='Dinero',max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Cajas"

    def __str__ (self):
        return f"{self.NumCaja}"
