from apps.movimiento.producto.models import Registro_Producto
from apps.movimiento.factura.models import Facturas, DetalleFactura
from django.db import transaction
from rest_framework.exceptions import ValidationError
from django.db.models import Sum

@transaction.atomic # esto protege la base de datos por si ocurre un error revierte todo
#funcion: tiene para parametros como: detalle_producto_id, cantidad_vendida "estos se llenan de todos en el view a traves del serializador"

def Validar_datos(datos_cantidad):
    
    cantidad= datos_cantidad.get('Cantidad')

    if cantidad is not None and cantidad <=0:
        raise ValidationError({"Cantidad": "La cantidad no puede se menor o igual a cero"})
    
    return True

def validar_existencia (detalle_Produto_Id, stock_solicitado):
    resultado= Registro_Producto.objects.filter(detalleProductoId_id=detalle_Produto_Id, Cantidad__gt=0, PrecioVenta__gt=0).aggregate(total=Sum('Cantidad'))

    total_stock=resultado['total'] or 0


    if stock_solicitado > total_stock :
        raise ValidationError({"Inventario": f"No hay suficiente stock. Solicitado: {stock_solicitado}, Disponible:{total_stock}" })

def suma_total(factura_id):
    resultado= DetalleFactura.objects.filter(FacturaId=factura_id).aggregate(total_calculado=Sum('Subtotal'))

    nuevo_total= resultado['total_calculado'] or 0
    factura = Facturas.objects.filter(id=factura_id).first()

    if factura:
        factura.Total = nuevo_total
        factura.save()
        print(f'Factura {factura_id} actualizada. Nuevo total: {factura.Total}')
    else:
        print('No se encontro factura')
def descontar_stock(detalle_producto_id, cantidad_vendida):
    #Buscar lotes antiguos
    # lotes es una variables= busca los productos solicitados en detalle de factura, busca los lotes con una cantidad mayor a 0
    # Y todos estos registros ordenados por fecha de registro, que a parece en la tabla registro_Producto
    lotes = Registro_Producto.objects.filter(detalleProductoId_id = detalle_producto_id, Cantidad__gt=0, PrecioVenta__gt=0).order_by('FechaRegistro')
    # Esto es para ver los resultados en consolas para saber si funciona adecuadamente
    # imprime los loste con relacion con el id de detalleProducto y los cuentas con la funcion count()
    print("Los lotes encontrados: ", lotes.count())

    # valor de cantidad_vendida se lo pasa en atraves del apis una ves consumida el serializador le pasa lo datos de la cantidad de datalleFactura
    # es decir en detalleFactura se venden 10 productos, es dato se lo pasa al variable cantidad_vendida
    # Y la vez se lo pasa a la otra variable que resta la cantidad en lote "cantidad_restante = cantidad_vendida "
    cantidad_restante = cantidad_vendida

    # comenzamos con el ciclo for que Pasa realmente lote es una variable que va a servir como contenedos de la variable lotes
    # lote in lotes , la variable lote, le pregruntas a la variable lotes que contiene el filtrado de la tabla registro_Producto
    # si contiene tienes un elemento en caso que si repite el ciclo, caso que no case la el ciclo 
    for lote in lotes:
        #Se imprime los datos en consola
        # lote como ya dije actua como un contenedor pro ende tiene los datos como id, Cantidad , estos datos bienen de variable Lotes que es un filtrador de la tabla registro_Producto
        print("Lote ID: ",lote.id)
        print("Cantidad antes: ", lote.Cantidad)

        # realiza una condicion si la variable cantidad_restante = cantidad_vendida , es 0, es decir si en detalle factura le dicen que la cantidad es 0
        #se detiene el ciclo si no hay cantidad que restar en inventario, con la funcion break
        if cantidad_restante <= 0:
            break

        #EL lote alcanza
        #si la cantidad de lote.Cantidad , decir la cantidad del registro_Producto >= cantidade_restante, detalleFactura
        #Si hay suficiente cantidad en el inventario(registro_Producto) se cumple esta condicion
        if lote.Cantidad >= cantidad_restante:
            #se va ir restando la cantidad de inventario(registro_Producto)
            lote.Cantidad -= cantidad_restante
            # se hace un insert en la base de datos 
            lote.save()
            #se imprime la cantidad en consola una vez restada la cantidad vendida, es decir muestra la actualización
            print("Cantidad después: ", lote.Cantidad)
            #la cantidad se reinicia a 0
            cantidad_restante = 0
        #lote no alcanza
        #
        else:
    
            cantidad_restante -= lote.Cantidad
            lote.Cantidad=0
            lote.save()
            print("Lote agotado")
    #validar inventario
    if(cantidad_restante > 0):
        raise Exception("No hay suficiente inventario")