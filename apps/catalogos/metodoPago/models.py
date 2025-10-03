from django.db import models

# Create your models here.
class Metodo_Pago (models.Model):
    tipo = models.CharField (verbose_name='Metodo de pago', max_length=50)

class Meta:
    verbose_name_plural = 'Metodos de pagos'

def __str__ (self):
    return f"{self.tipo}"