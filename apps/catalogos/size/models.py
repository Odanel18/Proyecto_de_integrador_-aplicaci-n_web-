from django.db import models

class Size (models.Model):
    Tamaño= models.CharField(verbose_name='Tamaño', max_length=50)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural= 'Sizes'

    def __str__ (self):
        return f"{self.Tamaño}"