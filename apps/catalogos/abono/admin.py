from django.contrib import admin
from apps.catalogos.abono.models import Abono

@admin.register(Abono)
class abonoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['facturaid', 'monto', 'cajaid','Fecha_Abono']
# Register your models here.
