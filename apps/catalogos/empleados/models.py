from django.db import models

# Create your models here.

class Empleado (models.Model):
    nombre = models.CharField(verbose_name='Nombres', max_length=100)
    apellido = models.CharField(verbose_name='Apellidos', max_length=100)
    telefono = models.CharField(verbose_name='Teléfono', max_length=8)
    num_Cedula = models.CharField(verbose_name='Numero de cédula', max_length=13, unique=True)

class Meta:
    verbose_name_plural= 'Empleados'

def __str__ (selt):
    return f"{selt.nombre} - {selt.apellido}"