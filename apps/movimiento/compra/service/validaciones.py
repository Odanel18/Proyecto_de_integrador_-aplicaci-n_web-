from rest_framework.validators import ValidationError
from apps.catalogos.proveedor.models import Proveedores
from apps.catalogos.condicionPago.models import CondicionPago
from apps.movimiento.producto.models import DetalleProductos

from datetime import date


def validar_compra(data):

    # Validar que la fecha de compra no esté vacía
    fecha_compra = data.get('Fecha')

    if not fecha_compra:
        raise ValidationError({
            "Fecha": "La fecha de compra es obligatoria."
        })

    # Validar que la fecha de compra no sea mayor a la fecha actual
    if fecha_compra > date.today():
        raise ValidationError({
            "Fecha": "La fecha de compra no puede ser mayor a la fecha actual."
        })

    # Validar que el número de compra no esté vacío
    if not data.get('NumCompra'):
        raise ValidationError({
            "NumCompra": "El número de compra no puede estar vacío."
        })

    # Validar que el proveedor no esté vacío
    proveedor = data.get('ProveedorId')

    if not proveedor:
        raise ValidationError({
            "ProveedorId": "El proveedor es obligatorio."
        })

    # Validar que el proveedor exista y esté activo
    if not Proveedores.objects.filter(
        id=proveedor.id,
        estado=True
    ).exists():

        raise ValidationError({
            "ProveedorId": "El proveedor seleccionado no existe."
        })

    # Validar que la condición de pago no esté vacía
    condicion_pago = data.get('CondicionPagoId')

    if not condicion_pago:
        raise ValidationError({
            "CondicionPagoId": "La condición de pago es obligatoria."
        })

    # Validar que la condición de pago exista y esté activa
    if not CondicionPago.objects.filter(
        id=condicion_pago.id,
        estado=True
    ).exists():

        raise ValidationError({
            "CondicionPagoId": "La condición de pago seleccionada no existe."
        })

    # Si la condición de pago es crédito
    if condicion_pago.descripcion.strip().lower() == 'credito':

        fecha_vencimiento = data.get('FechaVencimiento')

        if not fecha_vencimiento:
            raise ValidationError({
                "FechaVencimiento":
                "La fecha de vencimiento es obligatoria para compras a crédito."
            })

        # Validar que la fecha de vencimiento sea mayor que la fecha de compra
        if fecha_vencimiento <= fecha_compra:
            raise ValidationError({
                "FechaVencimiento":
                "La fecha de vencimiento debe ser mayor a la fecha de compra."
            })

    # Validar que haya por lo menos un detalle
    detalles = data.get('detallesCompra', [])

    if not detalles or not isinstance(detalles, list):
        raise ValidationError({
            "detalles_Compra":
            "Una compra debe tener al menos un producto en el detalle."
        })

    # Obtener los productos
    idproductos = [
        d.get('DetalleProductoId').id
        for d in detalles
        if d.get('DetalleProductoId')
    ]

    # No permitir productos repetidos
    if len(idproductos) != len(set(idproductos)):
        raise ValidationError({
            "detalles_Compra":
            "No se pueden repetir productos en el detalle de la compra."
        })

    # Validar cada detalle
    for index, detalle in enumerate(detalles):

        producto = detalle.get('DetalleProductoId')

        if not producto:
            raise ValidationError({
                f"detalles_Compra[{index}].DetalleProductoId":
                "El producto es obligatorio."
            })

        # Validar que el producto exista y esté activo
        if not DetalleProductos.objects.filter(
            id=producto.id,
            estado=True
        ).exists():

            raise ValidationError({
                f"detalles_Compra[{index}].DetalleProductoId":
                "El producto seleccionado no existe."
            })

        cantidad = detalle.get('Cantidad')
        precio_unitario = detalle.get('PrecioUnitario')

        if cantidad is None or cantidad <= 0:
            raise ValidationError({
                f"detalles_Compra[{index}].Cantidad":
                "La cantidad debe ser mayor a cero."
            })

        if precio_unitario is None or precio_unitario <= 0:
            raise ValidationError({
                f"detalles_Compra[{index}].PrecioUnitario":
                "El precio unitario debe ser mayor a cero."
            })