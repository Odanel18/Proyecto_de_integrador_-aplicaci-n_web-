from django.contrib import admin

from apps.catalogos.caja.models import Caja

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Num_caja']
    list_display = ['Saldo_Inicial', 'Ingreso', 'Egresos','Saldo_Final','Fecha','Num_caja','empleadoid','Dinero']
# Register your models here.
