from django.contrib import admin
from apps.catalogos.metodoPago.models import MetodoPago

@admin.register(MetodoPago)
class Metodo_PagoAdmin(admin.ModelAdmin):
    search_fields = ['id',]
    list_display = ['Tipo']
# Register your models here.
