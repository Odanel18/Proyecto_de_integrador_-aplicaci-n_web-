from django.contrib import admin

from apps.catalogos.compra.models import Compra

@admin.register(Compra)
class compraAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Num_Compra']
    list_display = ['Num_compra', 'metodo_Pagoid', 'Fecha']
# Register your models here.

