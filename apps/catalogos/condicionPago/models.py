from django.db import models

class CondicionPago (models.Model):
    descripcion = models.CharField (verbose_name="Descripcion", max_length= 50)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural:'CondicionPago'

    def __str__ (self):
        return f'{self.descripcion}'

