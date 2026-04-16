from django.db import models

# Create your models here.

class TipoMovimientoCaja (models.Model):
    Tipo=models.CharField(verbose_name='Tipo', max_length=50)

    class Meta:
        verbose_name_plural = 'Tipos'
    
    def __str__(self):
        return f"{self.Tipo}"
