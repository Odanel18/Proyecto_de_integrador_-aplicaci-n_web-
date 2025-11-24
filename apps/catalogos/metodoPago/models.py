from django.db import models

# Create your models here.
class MetodoPago (models.Model):
    Tipo = models.CharField (verbose_name='Metodo de pago', max_length=50)
    estado = models.BooleanField(default=True)
    class Meta:
      verbose_name_plural = 'Metodos de pago'

    def __str__ (self):
        return f"{self.Tipo}"