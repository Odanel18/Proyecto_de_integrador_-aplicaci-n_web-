from django.db import models
from apps.catalogos.marca.models import Marcas
# Create your models here.
class Motos (models.Model):
    Modelo = models.CharField(verbose_name='Modelos',max_length=60)
    Año = models.DateField (verbose_name='Año')
    MarcaId= models.ForeignKey (Marcas,verbose_name='Macar',on_delete=models.PROTECT)

class meta :
    verbose_name_plural='Motos'

def __str__ (self):
    return f"{self.Modelo}"