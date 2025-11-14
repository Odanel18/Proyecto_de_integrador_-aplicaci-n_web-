from django.db import models
from apps.catalogos.tipo.models import Tipo
# Create your models here.
class Marcas (models.Model):
    Nombre=models.CharField (verbose_name='Nombre', max_length=50)
    TipoId = models.ForeignKey(Tipo,verbose_name='Tipo', on_delete=models.PROTECT)

class meta:
    verbose_name_plural='Marcas'

def __str__ (self):
    return f"{self.Nombre}"