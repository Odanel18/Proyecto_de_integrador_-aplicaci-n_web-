from django.db import transaction
from rest_framework.exceptions import ValidationError
from apps.movimiento.compra.models import DetalleCompra
from apps.movimiento.producto.models import Registro_Producto



def validar_compra(datos):
    cantidad= datos.get('Cantidad')

    if cantidad is not None and cantidad <= 0:

        raise ValidationError({"Cantidad": "La cantidad no puede ser menor o igual a cero"})
    return True
        # raise ValidationError( "No se permiten cantidades menores o iguales a 0" )
      #for detalle in detalles:

     #   if detalle.Cantidad <= 0:
            
      #      raise ValidationError (f"No se acepta la cantidad del producto {detalle.detallProductoId}")

def aumentar_stock(detalle_ProductoId, cantidad, precio_unitario):
    precioVenta=0
    nuevo_lote=Registro_Producto.objects.create(detalleProductoId_id=detalle_ProductoId,Cantidad=cantidad, precioCompra=precio_unitario, PrecioVenta=precioVenta)

    print(f'Nuevo lote creado: ID {nuevo_lote}, con {cantidad} unidades. ')
    return nuevo_lote


