from django.contrib import admin
from apps.catalogos.estadoCuenta.models import EstadoCuenta

@admin.register(EstadoCuenta)
class EstadoCuentaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['descripcion']
# Register your models here.
