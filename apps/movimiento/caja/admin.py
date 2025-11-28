from django.contrib import admin

from apps.movimiento.caja.models import Caja

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumCaja']
    list_display = ['SaldoInicial', 'Ingresos', 'Egresos','SaldoFinal','FechaApertura','FechaCierre','NumCaja','EmpleadoId','Dinero']
# Register your models here.
