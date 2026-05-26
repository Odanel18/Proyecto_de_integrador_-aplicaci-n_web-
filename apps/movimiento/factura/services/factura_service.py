from apps.movimiento.producto.models import Registro_Producto
from django.db import transaction

@transaction.atomic
def descontar_stock(detalle_producto_id, cantidad_vendida):
    #Buscar lotes antiguos
    lotes = Registro_Producto.objects.filter(detalleProductoId_id = detalle_producto_id, Cantidad__gt=0).order_by('FechaRegistro')
    print("Los lotes encontrados: ", lotes.count())

    cantidad_restante = cantidad_vendida

    for lote in lotes:
        print("Lote ID: ",lote.id)
        print("Cantidad antes: ", lote.Cantidad)

        if cantidad_restante <= 0:
            break

        #EL lote alcanza
        if lote.Cantidad >= cantidad_restante:
            lote.Cantidad -= cantidad_restante

            lote.save()
            print("Cantidad después: ", lote.Cantidad)

            cantidad_restante = 0
        #lote no alcanza
        else:
            cantidad_restante -= lote.Cantidad
            lote.Cantidad=0
            lote.save()
            print("Lote agotado")
    #validar inventario
    if(cantidad_restante > 0):
        raise Exception("No hay suficiente inventario")