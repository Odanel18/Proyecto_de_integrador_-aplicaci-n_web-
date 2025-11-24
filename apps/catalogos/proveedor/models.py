from django.db import models

# Create your models here.
class Proveedores (models.Model):
    Nombre = models.CharField (verbose_name='Nombre', max_length=100)
    Telefono = models.CharField(verbose_name='Teléfono', max_length=10)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural= 'Proveedores'

    def __str__ (self):
        return f"{self.Nombre}"