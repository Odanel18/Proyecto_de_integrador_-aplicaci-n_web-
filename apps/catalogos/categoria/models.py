from django.db import models

# Create your models here.

class Categorias (models.Model):
    Nombre= models.CharField (verbose_name='Nombre',max_length=100)

class meta:
    verbose_name_plural='Çategorias'

def __str__ (self):
    return f"{self.Nombre}"