from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.movimiento.factura.models import Facturas, DetalleFactura, FacturasCredito
from apps.movimiento.caja.models import MovimientoCaja, TurnoCaja
from apps.movimiento.movimientoPago.models import MovimientoPago
from apps.catalogos.tipoMovimientoCaja.models import TipoMovimientoCaja
from apps.catalogos.metodoPago.models import MetodoPago
from apps.catalogos.estadoCuenta.models import EstadoCuenta
from apps.movimiento.producto.models import RegistroProducto

from .factura_service import Validar_datos, validar_existencia, descontar_stock

@transaction.atomic
def crear_factura_completa(datos_factura, detalles_data, pagos_data=None, datos_credito=None, turno_caja_id=None, tipo_movimiento_id=None):
    condicion_id = datos_factura['condicionId'].id if hasattr(datos_factura['condicionId'], 'id') else datos_factura['condicionId']

    # 1. Crear la Factura cabecera
    factura = Facturas.objects.create(
        NumFactura=datos_factura['NumFactura'],
        ClienteId=datos_factura['ClienteId'],
        condicionId=datos_factura['condicionId'],
        Total=0
    )

    total_acumulado = 0

    # 2. Registrar Detalles y descontar Stock
    for item in detalles_data:
        Validar_datos(item)
        lote_id = item['loteId']
        cantidad = item['Cantidad']
        
        validar_existencia(lote_id, cantidad)
        
        lote = RegistroProducto.objects.get(id=lote_id)
        precio_unitario = lote.PrecioVenta
        subtotal = cantidad * precio_unitario
        total_acumulado += subtotal

        DetalleFactura.objects.create(
            FacturaId=factura,
            loteId=lote,
            Cantidad=cantidad,
            PrecioUnitario=precio_unitario,
            Subtotal=subtotal
        )

        descontar_stock(lote_id, cantidad)

    # Actualizar Total real de Factura
    factura.Total = total_acumulado
    factura.save()

    # 3. Flujo Al Contado (ID 1)
    if condicion_id == 1:
        if not pagos_data or not turno_caja_id or not tipo_movimiento_id:
            raise ValidationError({"error": "Las ventas al contado requieren turno de caja, tipo de movimiento y pagos."})

        total_pagos = sum(pago['monto'] for pago in pagos_data)
        if total_pagos != total_acumulado:
            raise ValidationError({
                "Pagos": f"El total pagado ({total_pagos}) no coincide con el total de la factura ({total_acumulado})."
            })

        turno = TurnoCaja.objects.get(id=turno_caja_id)
        tipo_mov = TipoMovimientoCaja.objects.get(id=tipo_movimiento_id)

        movimiento_caja = MovimientoCaja.objects.create(
            fecha=timezone.now(),
            descripcion=f"Venta Contado Factura #{factura.NumFactura}",
            monto=total_acumulado,
            tipoMovimientoCajaId=tipo_mov,
            facturaid=factura,
            turnoCajaId=turno
        )

        for pago in pagos_data:
            metodo = MetodoPago.objects.get(id=pago['metodoPagoId'])
            MovimientoPago.objects.create(
                monto=pago['monto'],
                metodoPagoId=metodo,
                MovimientoCajaId=movimiento_caja
            )
 
    # 4. Flujo Al Crédito (ID 2)
    elif condicion_id == 2:
        if not datos_credito:
            raise ValidationError({"credito": "Faltan los datos necesarios para registrar el crédito."})

        estado_cuenta = EstadoCuenta.objects.get(id=datos_credito['estadoCuentaId'])

        # Crear primero el registro de crédito
        credito = FacturasCredito.objects.create(
            FacturaId=factura,
            FechaInicioCredito=timezone.now(),
            montoTotalCredito=total_acumulado,
            saldoPendiente=total_acumulado,
            FechaLimiteCredito=datos_credito['FechaLimiteCredito'],
            estadoCuentaId=estado_cuenta
        )

        # Registrar el movimiento informativo en caja si se envía el turno
        if turno_caja_id and tipo_movimiento_id:
            turno = TurnoCaja.objects.get(id=turno_caja_id)
            tipo_mov = TipoMovimientoCaja.objects.get(id=tipo_movimiento_id)

            MovimientoCaja.objects.create(
                fecha=timezone.now(),
                descripcion=f"Venta Crédito Factura #{factura.NumFactura}",
                monto=0.00,  # 0.00 para no sumar en efectivo de caja, o total_acumulado según prefieras
                tipoMovimientoCajaId=tipo_mov,
                facturaid=factura,
                facturaCreditoId=credito,  # Enlazamos el ID de la factura a crédito
                turnoCajaId=turno
            )

    else:
        raise ValidationError({"condicionId": "Condición de pago no válida."})

    return factura