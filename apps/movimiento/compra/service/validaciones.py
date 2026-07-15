from apps.movimiento.producto.models import DetalleProductos, Registro_Producto
from apps.movimiento.compra.models import Compras, DetalleCompra
from django.db import transaction
from rest_framework.exceptions import ValidationError
from django.db.models import Sum, Q


# ------------------------------------------------------------------
# VALIDACIONES BÁSICAS DEL ITEM (igual filosofía que factura_service)
# ------------------------------------------------------------------
def validar_datos(item):
    """
    Valida que la cantidad y el precio unitario vengan correctos.
    'item' es el diccionario que llega directo desde el request (uno por
    cada producto que se está comprando).
    """
    cantidad = item.get('Cantidad')
    precio_unitario = item.get('PrecioUnitario')

    if cantidad is None:
        raise ValidationError({"Cantidad": "La cantidad es obligatoria"})

    if cantidad <= 0:
        raise ValidationError({"Cantidad": "La cantidad no puede ser menor o igual a cero"})

    if precio_unitario is not None and precio_unitario <= 0:
        raise ValidationError({"PrecioUnitario": "El precio unitario no puede ser menor o igual a cero"})

    return True


# ------------------------------------------------------------------
# BÚSQUEDA DE PRODUCTO POR NOMBRE / CÓDIGO (en lugar del id)
# ------------------------------------------------------------------
def resolver_detalle_producto(item):
    """
    Permite que el usuario identifique el producto que está comprando sin
    tener que conocer el id interno de DetalleProductos.

    El front puede enviar cualquiera de estas formas en cada item:

    1) Por id (forma "clásica", se sigue soportando):
       {"detallProductoId": 5, "Cantidad": 10, "PrecioUnitario": 25}

    2) Por nombre / código del producto:
       {"producto": "Casco MT", "Cantidad": 10, "PrecioUnitario": 25}
       {"producto": "CAS-001", "Cantidad": 10, "PrecioUnitario": 25}

    3) Si ese producto tiene varias variantes (distinta marca, moto o talla)
       hay que desambiguar agregando uno o varios de estos campos:
       {"producto": "Casco MT", "marca": "MT Helmets", "moto": "Pulsar 200",
        "size": "M", "Cantidad": 10, "PrecioUnitario": 25}

    Devuelve la instancia de DetalleProductos encontrada, o lanza
    ValidationError con un mensaje claro si no se encuentra o es ambiguo.
    """

    # 1) Si ya viene el id, lo respetamos (compatibilidad hacia atrás)
    detalle_id = item.get('detallProductoId')
    if detalle_id:
        try:
            return DetalleProductos.objects.get(pk=detalle_id, estado=True)
        except DetalleProductos.DoesNotExist:
            raise ValidationError({"detallProductoId": f"No existe un producto con id {detalle_id}"})

    # 2) Buscamos por nombre o código de producto
    nombre_producto = item.get('producto') or item.get('Producto')

    if not nombre_producto:
        raise ValidationError({
            "producto": "Debes indicar el producto a comprar (por nombre, código o id)."
        })

    queryset = DetalleProductos.objects.filter(estado=True).filter(
        Q(producto__Nombre__iexact=nombre_producto) | Q(producto__Codigo__iexact=nombre_producto)
    )

    # 3) Filtros opcionales para desambiguar variantes del mismo producto
    marca = item.get('marca') or item.get('Marca')
    moto = item.get('moto') or item.get('Moto')
    size = item.get('size') or item.get('Size') or item.get('talla')

    if marca:
        queryset = queryset.filter(MarcaId__Nombre__iexact=marca)
    if moto:
        queryset = queryset.filter(MotoId__Modelo__iexact=moto)
    if size:
        queryset = queryset.filter(size__descripcion__iexact=size)

    total = queryset.count()

    if total == 0:
        raise ValidationError({
            "producto": f"No se encontró el producto '{nombre_producto}'. "
                        f"Verifica el nombre/código o agrega marca, moto y/o talla."
        })

    if total > 1:
        opciones = [
            f"id {d.id} ({d.MarcaId.Nombre} - {d.MotoId.Modelo}"
            f"{' - ' + d.size.descripcion if d.size else ''})"
            for d in queryset
        ]
        raise ValidationError({
            "producto": f"El producto '{nombre_producto}' tiene varias variantes, "
                        f"especifica marca, moto y/o talla para identificarlo. "
                        f"Opciones encontradas: {', '.join(opciones)}"
        })

    return queryset.first()


# ------------------------------------------------------------------
# CÁLCULOS Y MOVIMIENTOS DE STOCK
# ------------------------------------------------------------------
def calcular_subtotal(cantidad, precio_unitario):
    return cantidad * precio_unitario


def suma_total(compra_id):
    resultado = DetalleCompra.objects.filter(CompraId=compra_id, estado=True).aggregate(
        total_calculado=Sum('Subtotal')
    )
    nuevo_total = resultado['total_calculado'] or 0

    compra = Compras.objects.filter(id=compra_id).first()
    if compra:
        compra.Total = nuevo_total
        compra.save()
        print(f'Compra {compra_id} actualizada. Nuevo total: {compra.Total}')
    else:
        print('No se encontró la compra')


def aumentar_stock(detalle_producto_id, cantidad, precio_unitario, precio_venta=0):
    """
    Cada compra genera un nuevo lote de inventario (Registro_Producto),
    igual que antes, pero ahora centralizado en el servicio.
    """
    nuevo_lote = Registro_Producto.objects.create(
        detalleProductoId_id=detalle_producto_id,
        Cantidad=cantidad,
        precioCompra=precio_unitario,
        PrecioVenta=precio_venta,
    )
    print(f'Nuevo lote creado: ID {nuevo_lote.id}, con {cantidad} unidades.')
    return nuevo_lote
