from django.contrib import admin

from apps.movimiento.caja.models import Caja , MovimientoCaja

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumCaja']
    list_display = ['SaldoInicial', 'Egresos','SaldoFinal','FechaApertura','FechaCierre','NumCaja','EmpleadoId','Din_efectivo','Din_digital']
# Register your models here.

@admin.register(MovimientoCaja)
class MovimientoCajaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'cajaId']
    list_display = ['fecha','tipoMovimientoCajaId', 'monto','facturaid', 'compraid', 'descripcion']
                    

