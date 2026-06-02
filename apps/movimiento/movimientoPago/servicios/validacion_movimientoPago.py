from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.movimiento.caja.models import Caja
from apps.movimiento.caja.models import MovimientoCaja

from apps.movimiento.factura.models import Facturas
from apps.movimiento.movimientoPago.models import MovimientoPago

from apps.catalogos.metodoPago.models import MetodoPago
from apps.catalogos.tipoMovimientoCaja.models import TipoMovimientoCaja
from apps.catalogos.origenSaldo.models import OrigenSaldo

from apps.catalogos.empleados.models import Empleados


@transaction.atomic
def registrar_pago(
    #empleado_id,
    factura_id,
    monto,
    metodo_pago_id,
    tipo_movimiento_id,
    origen_saldo_id
):
    #empleado= Empleados.objects.get(id=empleado_id)
    # =====================================
    # VALIDAR CAJA ABIERTA
    # =====================================

    caja = Caja.objects.filter(
        #EmpleadoId=empleado,
        abierta=True,
        estado=True
    ).first()

    if not caja:

        raise ValidationError(
            "No tiene una caja abierta"
        )

    # =====================================
    # VALIDAR FACTURA
    # =====================================

    factura = Facturas.objects.filter(
        id=factura_id,
        estado=True
    ).first()

    if not factura:

        raise ValidationError(
            "Factura no encontrada"
        )

    # =====================================
    # CALCULAR TOTAL PAGADO
    # =====================================

    pagos = MovimientoPago.objects.filter(
        facturaId=factura,
        estado=True
    )

    total_pagado = sum(
        pago.monto for pago in pagos
    )

    saldo_pendiente = factura.Total - total_pagado

    # =====================================
    # VALIDAR MONTO
    # =====================================

    if monto > saldo_pendiente:

        raise ValidationError(
            "El pago excede el saldo pendiente"
        )

    # =====================================
    # BUSCAR RELACIONES
    # =====================================

    metodo_pago = MetodoPago.objects.get(
        id=metodo_pago_id
    )

    tipo_movimiento = TipoMovimientoCaja.objects.get(
        id=tipo_movimiento_id
    )

    origen_saldo = OrigenSaldo.objects.get(
        id=origen_saldo_id
    )

    # =====================================
    # CREAR MOVIMIENTO PAGO
    # =====================================

    movimiento_pago = MovimientoPago.objects.create(

        monto=monto,

        fecha=timezone.now(),

        metodoPagoId=metodo_pago,

        facturaId=factura,

        tipoMovimientoCajaId=tipo_movimiento,

        origenSaldoId=origen_saldo,

        estado=True
    )

    # =====================================
    # CREAR MOVIMIENTO CAJA
    # =====================================

    MovimientoCaja.objects.create(

        cajaId=caja,

        fecha=timezone.now(),

        tipoMovimientoCajaId=tipo_movimiento,

        monto=monto,

        facturaid=factura,

        descripcion=f"Pago factura #{factura.NumFactura}"
    )

    # =====================================
    # ACTUALIZAR DINERO EN CAJA
    # =====================================

    # ejemplo:
    # 1 = efectivo
    # 2 = transferencia

    if metodo_pago.id == 5:

        caja.Din_efectivo += monto

    else:

        caja.Din_digital += monto

    # actualizar saldo final

    caja.SaldoFinal = (
        caja.SaldoInicial
        + caja.Din_efectivo
        + caja.Din_digital
        - caja.Egresos
    )

    caja.save()

    return movimiento_pago