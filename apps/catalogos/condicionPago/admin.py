from django.contrib import admin
from apps.catalogos.condicionPago.models import CondicionPago

@admin.register(CondicionPago)
class CondicionPagoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['descripcion']
# Register your models here.
