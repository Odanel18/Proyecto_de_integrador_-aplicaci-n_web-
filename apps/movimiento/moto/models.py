from django.db import models
from apps.movimiento.marca.models import Marcas

class Motos (models.Model):
    Modelo = models.CharField(verbose_name='Modelos',max_length=60)
    Año = models.IntegerField (verbose_name='Año')
    MarcaId= models.ForeignKey (Marcas,verbose_name='Macar',on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)
    
    class Meta :
        verbose_name_plural='Motos'

    def __str__ (self):
        return f"{self.Modelo}"