from django.contrib import admin
from apps.catalogos.origenSaldo.models import OrigenSaldo

@admin.register(OrigenSaldo)
class OrigenSaldoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['descripcion']
# Register your models here.
