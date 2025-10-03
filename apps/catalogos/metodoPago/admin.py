from django.contrib import admin
from apps.catalogos.metodoPago.models import Metodo_Pago

@admin.register(Metodo_Pago)
class Metodo_PagoAdmin(admin.ModelAdmin):
    search_fields = ['id',]
    list_display = ['tipo']
# Register your models here.
