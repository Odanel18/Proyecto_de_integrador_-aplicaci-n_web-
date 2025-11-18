from django.contrib import admin
from apps.movimiento.moto.models import Motos

@admin.register(Motos)
class MotoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Modelo', 'Año','MarcaId']
# Register your models here.
