from django.db import models

# Create your models here.
class Tipo (models.Model):
    Tipo_Marca=models.CharField(verbose_name='Tipo de marca', max_length=50)

class meta:
    verbose_name_plural='Tipos'

def __str__ (self):
    return f"{self.Tipo_Marca}"