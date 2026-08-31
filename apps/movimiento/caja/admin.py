from django.contrib import admin

from apps.movimiento.caja.models import TurnoCaja , MovimientoCaja,Caja

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumCaja']
    list_display = ['NumCaja','abierta']

@admin.register(TurnoCaja)
class TurnoCajaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['FechaApertura', 'FechaCierre', 'SaldoInicial', 'Egresos','Din_efectivo', 'Din_digital','SaldoFinal','abierto']

@admin.register(MovimientoCaja)
class MovimientoCajaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'turnoCajaId']
    list_display = ['fecha','turnoCajaId','tipoMovimientoCajaId', 'monto','facturaid', 'compraid', 'descripcion','compraCreditoId','facturaCreditoId']
                    
               

