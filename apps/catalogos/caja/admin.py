from django.contrib import admin

from apps.catalogos.caja.models import Caja

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumCaja']
    list_display = ['SaldoInicial', 'Ingresos', 'Egresos','SaldoFinal','Fecha','NumCaja','EmpleadoId','Dinero']
# Register your models here.
