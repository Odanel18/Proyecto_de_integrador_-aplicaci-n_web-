from django.db import transaction

from apps.movimiento.compra.models import Compras, DetalleCompra, ComprasCredito
from apps.movimiento.producto.models import RegistroProducto
from apps.catalogos.estadoCuenta.models import EstadoCuenta


class CompraService:

    @staticmethod
    def crear_Compra(data):

        fecha = data['Fecha']
        numero = data['NumCompra']
        proveedores = data['ProveedorId']
        condicion = data['CondicionPagoId']
        detalles = data['detallesCompra']
        fecha_vencimiento = data.get('FechaVencimiento')

        with transaction.atomic():

            # CREAR LA COMPRA

            compra = Compras.objects.create(
                Fecha=fecha,
                NumCompra=numero,
                Total=0,
                ProveedorId=proveedores,
                CondicionPagoId=condicion
            )

            total = 0
            detalles_crear = []

            # PREPARAR LOS DETALLES

            for detalle in detalles:

                cantidad = detalle["Cantidad"]
                precioUnitario = detalle["PrecioUnitario"]
                producto = detalle["DetalleProductoId"]

                subtotal = cantidad * precioUnitario

                detalle_obj = DetalleCompra(
                    Cantidad=cantidad,
                    PrecioUnitario=precioUnitario,
                    Subtotal=subtotal,
                    CompraId=compra,
                    DetalleProductoId=producto
                )

                detalles_crear.append(detalle_obj)

                total += subtotal

            # BULK CREATE DE DETALLE COMPRA

            DetalleCompra.objects.bulk_create(detalles_crear)

            # OBTENER LOS DETALLES YA GUARDADOS

            detalles_insertados = list(
                DetalleCompra.objects.filter(
                    CompraId=compra
                ).order_by('id')
            )

            # PREPARAR REGISTRO PRODUCTO

            lotes_crear = []

            for det, datos_detalle in zip(
                detalles_insertados,
                detalles
            ):

                lotes_crear.append(
                    RegistroProducto(
                        Cantidad=det.Cantidad,
                        precioCosto=det.PrecioUnitario,
                        PrecioVenta=datos_detalle['PrecioVenta'],
                        DetalleCompraId=det
                    )
                )

            # BULK CREATE DE REGISTRO PRODUCTO

            RegistroProducto.objects.bulk_create(lotes_crear)

            # ACTUALIZAR TOTAL DE LA COMPRA

            compra.Total = total
            compra.save()

            # SI ES CRÉDITO, CREAR CUENTA

            if condicion.descripcion.strip().lower() == 'credito':

                estado_pendiente = EstadoCuenta.objects.get(
                    descripcion__iexact='Pendiente',
                    estado=True
                )

                ComprasCredito.objects.create(
                    MontoTotal=total,
                    SaldoPendiente=total,
                    FechaInicio=fecha,
                    FechaVencimiento=fecha_vencimiento,
                    CompraId=compra,
                    EstadoCuentaId=estado_pendiente
                )

        return compra