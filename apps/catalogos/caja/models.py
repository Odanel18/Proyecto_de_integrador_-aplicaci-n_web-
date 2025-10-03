from django.db import models

# Create your models here.
from apps.catalogos.empleados.models import Empleado

class Caja (models.Model):
    Saldo_Inicial= models.IntegerField(verbose_name='Saldo inicial')
    Ingreso = models.IntegerField(verbose_name='Ingreso')
    Egresos = models.IntegerField(verbose_name='Egresos')
    Saldo_Final = models.IntegerField (verbose_name='Saldo final')
    Fecha = models.DateTimeField()
    Num_caja= models.IntegerField(verbose_name='Numero de caja')
    empleadoid = models.ForeignKey(Empleado,verbose_name='Empleados', on_delete=models.PROTECT)
    Dinero = models.DecimalField (verbose_name='Dinero',max_digits=10, decimal_places=2)

class Meta:
    verbose_name_plural='Caja'

def __str__ (self):
    return f"{self.Num_caja}"
