from django.db import models

# Create your models here.
class Proveedor (models.Model):
    nombre = models.CharField (verbose_name='Nombre', max_length=100)
    telefono = models.CharField(verbose_name='Teléfono', max_length=10)

class Meta:
    verbose_name_plural= 'Proveedores'

def __str__ (self):
    return f"{self.nombre}"