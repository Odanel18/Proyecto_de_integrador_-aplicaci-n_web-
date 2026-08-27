from django.db import transaction
from django.db.models import Sum
from rest_framework.exceptions import ValidationError
from apps.movimiento.producto.models import RegistroProducto
from apps.movimiento.factura.models import Facturas, DetalleFactura

def Validar_datos(datos_cantidad):
    cantidad = datos_cantidad.get('Cantidad')
    if cantidad is not None and cantidad <= 0:
        raise ValidationError({"Cantidad": "La cantidad no puede ser menor o igual a cero"})
    return True

def validar_existencia(lote_id, stock_solicitado):
    resultado = RegistroProducto.objects.filter(
        id=lote_id, Cantidad__gt=0, PrecioVenta__gt=0
    ).aggregate(total=Sum('Cantidad'))
    
    total_stock = resultado['total'] or 0
    if stock_solicitado > total_stock:
        raise ValidationError({
            "Inventario": f"No hay suficiente stock. Solicitado: {stock_solicitado}, Disponible: {total_stock}"
        })

def descontar_stock(lote_id, cantidad_vendida):
    lotes = RegistroProducto.objects.filter(
        id=lote_id, Cantidad__gt=0, PrecioVenta__gt=0
    ).order_by('FechaRegistro')
    
    cantidad_restante = cantidad_vendida
    for lote in lotes:
        if cantidad_restante <= 0:
            break
        if lote.Cantidad >= cantidad_restante:
            lote.Cantidad -= cantidad_restante
            lote.save()
            cantidad_restante = 0
        else:
            cantidad_restante -= lote.Cantidad
            lote.Cantidad = 0
            lote.save()
            
    if cantidad_restante > 0:
        raise ValidationError({"Inventario": "No hay suficiente inventario en los lotes."})